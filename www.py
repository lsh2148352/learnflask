from flask import Flask
from index import index_page
from test1 import app


app.register_blueprint(index_page,url_prefix="/l")

