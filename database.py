from fastapi import FastAPI
import mysql.connector

db = mysql.connector.connect(
    host="localhost",  # Cambia 'db' a 'localhost'
    user='root',
    password='root',
    database='inventario',
    port=3308  # Puerto externo mapeado en docker-compose.yml
)