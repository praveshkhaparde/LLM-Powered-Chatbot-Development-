import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from sentence_transformers import SentenceTransformer
from Local_Embedding_Class import LocalEmbeddings

# Load environment variables
load_dotenv()

# Initialize Sentence Transformer and custom embedder
sent_trans = SentenceTransformer('Sent_Transformer_Mod')
embedder = LocalEmbeddings('From_Local_Trans', from_local=True, emb_mod=sent_trans)

# Load the FAISS vector store
print('Loading vector store...')
vs = FAISS.load_local('new_ug_book', embedder, allow_dangerous_deserialization=True)
print('Vector store loaded.')

# Initialize retriever with similarity search
retriever = vs.as_retriever(type='similarity', search_kwargs={'k': 4})

# Define function to format retrieved documents
def format_docs(retrieved_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return context_text

# Initialize conversation memory
memory = ConversationBufferMemory(memory_key="history", return_messages=True)

# Define prompt template
prompt = PromptTemplate(
    template="""
    You are a helpful assistant.
    Answer USING MARKDOWN SYNTAX about the UG academic rules of IITB ONLY from the provided transcript context.
    Remember questions that you've been asked in a chat.
    If the context is insufficient, just say you don't know. Don't start the sentences with "according to the transcript provided" or "according to context provided".
    NEVER make it appear that you've been provided a context. When you want to quote the context, say "According to the UGAC Rulebook, "
    {context}
    Question: {question}
    """,
    input_variables=['context', 'question']
)

# Initialize LLM with memory
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.5, model_kwargs={"memory": memory})

# Initialize output parser
parser = StrOutputParser()

# Define parallel chain for processing
par_chain = RunnableParallel(
    {
        'context': retriever | RunnableLambda(format_docs),
        'question': RunnablePassthrough()
    }
)

# Define main chain with memory
main_chain = par_chain | prompt | llm | parser

print('Main chain ready!')
print("Hey, you can ask me anything about the UGAC Rulebook!!:)")
while True:
    query = input()
    resp = main_chain.invoke(query)
    print(f'Bot: {resp}')
    print('Anything Else?')