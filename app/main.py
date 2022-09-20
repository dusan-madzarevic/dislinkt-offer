import uvicorn
from pymongo import MongoClient
from starlette.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from app.models import Offer
import os
import time

start = time.time()


DB_USERNAME = os.getenv('DB_USERNAME', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_CONTAINER_NAME = os.getenv('DB_CONTAINER_NAME', 'offer_container')
DB_PORT = os.getenv('DB_PORT', '27017')
DB_NAME = os.getenv('DB_NAME', 'offers')

app = FastAPI()

client = MongoClient(f'mongodb://{DB_CONTAINER_NAME}:{DB_PORT}/{DB_NAME}?authSource=admin',
                     username=DB_USERNAME, password=DB_PASSWORD)


db = client.offers
collection = db.offer


app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_methods="*",
    allow_headers="*",
)


@app.get("/")
def read_root():
    data = client['offers']
    cole = data['offer']
    cole.insert_one({"postition": "junior", "description": "devops", "conditions": "knowledge"}) # list(collection.find({}))
    print(collection)
    #return client.server_info()

    return client.list_database_names()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #uvicorn.run(app, port=8000, host="0.0.0.0")
    # print(Offer.objects().to_json())
    print("merhaba")
    print(list(collection.find({})))

