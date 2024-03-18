from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text
import os


from dotenv import load_dotenv
print(load_dotenv())


app = FastAPI()
@app.get("/")
def inicio():
    print(os.getenv('API_KEY'))
    return {"message": "Esta es una Api para realizar consultas a OpenAI"}