import logging
import azure.functions as func
from FastAPIApp import app
from doc_vector_store import create_new_index  # Main API application
from qa_bot import qaBot
from pydantic import BaseModel

class Item(BaseModel):
    query: str
    index_name: str

class Pinecone(BaseModel):
    index_name: str



@app.get("/sample")
async def index():
    return {
        "info": "Try /hello/Shivani for parameterized route.",
    }


@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }


# post method to create the new index in pinecone by providing the index name
@app.post("/create_index")
async def create_index(Pinecone: Pinecone):
    return {
        "response": create_new_index(Pinecone.index_name),
    }

# write the post method for the api to use function to qa_bot.py
#  qaBot(query, index_name)
@app.post("/qa")
async def get_answer(Item: Item):
    return {
        "answer": qaBot(Item.query, Item.index_name),
    }


async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req, context)