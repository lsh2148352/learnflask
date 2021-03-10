from flask import Flask
from index import index_page

app = Flask(__name__)
app.register_blueprint(index_page,url_prefix="/l")

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
    # c = {"l":"123"}
    # print(c)
    # c["u"] = {"name":"lanzi","qq":"456"}
    # print(c)
