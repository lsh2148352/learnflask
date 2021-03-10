from flask import Flask,Blueprint


index_page = Blueprint("index_page",__name__)

@index_page.route("/1")
def test1():
    return "hello 1"

@index_page.route("/2")
def test2():
    return"hello 2"