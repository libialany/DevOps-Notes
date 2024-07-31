import os
from dotenv import load_dotenv
load_dotenv() 
from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


origins = [
    # os.environ.get('URL_FRONTEND')
    # "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello/{username}")
async def read_repo(username: str):
    return {"data": "Hello {}".format(username)}

@app.get("/hello-ai/{username}")
async def read_repo(username: str):
    return {"data": "Hello 🤖🤖🤖 {}".format(username)}

