from flask import Flask
from flask_sqlalchemy import SQLAlchemy#数据库配置

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:968574@127.0.0.1/mysql'
db1 = SQLAlchemy(app)

# if __name__=='__main__':
#     app.run(host='127.0.0.1',port=5000,debug=True)
#     # c = {"l":"123"}
#     # print(c)
#     # c["u"] = {"name":"lanzi","qq":"456"}
#     # print(c)
