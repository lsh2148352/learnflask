from flask import Flask,Blueprint,request


index_page = Blueprint("index_page",__name__)

@index_page.route("/1",methods = ["GET"])
def test1():
    re = request.values
    return re["a"] if "a" in re else "hello 112"

@index_page.route("/2",methods = ["GET","POST"])
def test2():
    re = request.values#get和post都可以
    return re["a"] if "a" in re else "hello 112"

@index_page.route("/upload",methods = ["POST"])
def test3():
    re = request.files['file']  if "file" in request.files else None#这里要跟上传参数的键名一致
    return "%s"%(re)