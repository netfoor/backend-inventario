from fastapi import FastAPI
import mysql.connector


db = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password = '',
    database = 'inventario',
    consume_results = True
)
