"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrqjfpmbg5e4kht2b7g-a.oregon-postgres.render.com",
        database="todo_zoez",
        user="todo_zoez_user",
        password="rrdqJW7Twl0dbj4uWfuhCyEZinrAalGw")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
