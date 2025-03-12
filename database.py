from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
db_url = os.getenv('DB_URL')

client = MongoClient(db_url)

db = client['Inventario']