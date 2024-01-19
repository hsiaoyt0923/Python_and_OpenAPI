from fastapi import FastAPI
import redis
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'), decode_responses=True)

@app.get("/")
def read_root():
    counter = redis_conn.incr('test:increment', 1)
    return {"Counter": counter}

@app.get("/counter/{c}")
def read_counter(c:int):
    counter = redis_conn.incr('test:increment', c)
    return {"Counter": counter}

@app.get("/temperature/{celsius}")
def save_temperature(celsius:float):
    redis_conn.set('board:temp', celsius)

@app.get("/temperature")
def read_temperature():
    celsius = redis_conn.get('board:temp')
    return {"Temperature": celsius}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}