from fastapi import FastAPI
from pydantic import BaseModel
from main_chain import main_chain

class Query(BaseModel):
    query: str

app = FastAPI()

@app.post("/ask")
async def ask(q: Query):
    print(q)
    resp = main_chain.invoke(q.query)
    return {"answer": resp}
