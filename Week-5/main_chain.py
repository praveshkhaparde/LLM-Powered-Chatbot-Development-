from dotenv import load_dotenv
from Local_Embedding_Class import LocalEmbeddings
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

load_dotenv()
sent_trans = SentenceTransformer('Sent_Transformer_Mod')
embedder = LocalEmbeddings('From_Local_Trans', from_local=True, emb_mod=sent_trans)
print('loading....')
vs = FAISS.load_local('new_ug_book', embedder, allow_dangerous_deserialization=True)
print('Vector Store is up')
retriever = vs.as_retriever(type = 'similarity', search_kwargs = {'k': 4})


par_chain = RunnableParallel(
    {
        'context': retriever | RunnableLambda(format_docs),
        'question': RunnablePassthrough()
    }
)

### A prompt that didn't work lol:
# You are a helpful assistant, please be polite.
#       Answer about the UG academic rules of IITB ONLY from the provided transcript context.
#       Do not say anything like "According to the document" or "It is mentioned in the transcript".
#       If nothing relevant at all in the context, say "Bruh, weird question, I don't know somehow XD", but if you find something relevant, you MUST ans
#       Context: {context}
                        
#       Question: {question}

prompt = PromptTemplate(template = """
      You are a helpful assistant.
      Answer USING MARKDOWN SYNTAX about the UG academic rules of IITB ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.Don't start the sentences with "according to the transcript provided" or "according to context provided"
      NEVER make it appear that you've been provided a context. When you want to quote the context, say "According to the UGAC Rulebook, "
      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.5)
parser = StrOutputParser()
main_chain = par_chain | prompt | llm | parser

print('Main_Chain Ready!')