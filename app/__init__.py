"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch1336j3cv203buhmbq0-a.oregon-postgres.render.com",
        database="todo_n0ra",
        user="todo_n0ra_user",
        password="R7uXYojyG3aR4YQLUZ7FDEqIQce5MV7z")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
