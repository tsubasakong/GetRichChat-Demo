import os
from langchain.embeddings.openai import OpenAIEmbeddings
#  create embedding class
# get the OPENAI_API_KEY from env 
def get_embeddings():
    # OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') 
    OPENAI_API_KEY=os.environ["OPENAI_API_KEY"]

    return OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)