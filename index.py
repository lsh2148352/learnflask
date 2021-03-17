from flask import Flask,Blueprint,request,make_response,jsonify,render_template
#Flask是主要的类 Blueprint是蓝图的类 request是接受请求的模块 make_response是相应请求的模块 render_template是用模板相应的模块
from test1 import db1
from sqlalchemy import text
from common.models.user import User


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

@index_page.route("/xytest",methods=["GET"])
def test4():
    data = {"a":"b"}
    re = make_response(jsonify(data))
    return re

@index_page.route("/xymbtest",methods=["GET"])
def test5():
    # sql = text("select * from `user`")
    # result = db1.engine.execute(sql)
    # result = [1,2,3]
    result = User.query.all()
    print(result[1])
    context = {"result":result}
    return render_template('hello.html',**context)