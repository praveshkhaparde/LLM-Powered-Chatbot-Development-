## Week 5

This week, I learned about the **Retrieval-Augmentation-Generation (RAG)** pipeline, which follows the stages:  
**Indexation → Retrieval → Augmentation → Generation**

---

### Directory Contents

#### `LangChain_YT_bot.ipynb`
- Implements a RAG pipeline for a YouTube video transcript.
- Transcript is stored in `transcript.txt`.
- Based on a code-along tutorial.

#### `ug_rulebook_rag.ipynb`
- RAG pipeline implementation for the UG Rulebook.
- Includes document loading, vector store creation and persistence, and `main_chain` setup and testing.

#### `ugac_rb/` and `new_ug_book/`
- Contain `.faiss` and `.pkl` files for vector stores created for the UG Rulebook.

---

### Major Milestone Files

- `Sentence_Transformer_Saver.py`:  
  Loads and locally saves the transformer model used for embeddings (both document and query).

- `main_chain.py`:  
  Sets up the RAG chain by loading the vector store, initializing the Gemini API client, and exposing the chain as `main_chain`.

- `bot_interface.py`:  
  Terminal-based chat application to test the working of `main_chain`.

- `app.py`:  
  Python (FastAPI) backend to handle POST requests with user queries and return RAG-based responses using `main_chain`.

- `server.js`:  
  Node.js backend script that sends user-submitted queries to `app.py` and receives the responses.

- `script.js`:  
  Frontend script for handling user input, appending messages to the DOM, and displaying bot responses.

- `index.html`:  
  Webpage interface for interacting with the bot.

- `styles.css`:  
  Stylesheet for UI design and layout.

---

### Experimental

- `main_chain_mem.py`:  
  Terminal chat application exploring a memory-augmented version of `main_chain`.  
  *(Still under development — even without memory, current RAG results are promising.)*
