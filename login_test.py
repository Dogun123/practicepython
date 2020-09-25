from flask import Flask,jsonify,request,render_template,make_response
from flask_cors import CORS
import requests

app = Flask(__name__,static_url_path='/static')
CORS(app)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler #logging 핸들러 이름을 적어줌
    file_handler = RotatingFileHandler(
        'dave_server.log',maxBytes=2000,backupCount=10)
    file_handler.setLevel(logging.WARNING) #어느 단계까지 로깅을 할지를 적어줌
    # app.logger.addHandler() 에 등록시켜줘야 app.logger로 사용 가능
    app.logger.addHandler(file_handler)

@app.errorhandler(404) #없는 페이지 요청했을 때 에러
def page_not_found(error):
    app.logger.error(error)
    return "<h1>해당 경로에 맞는 웹페이지가 없습니다. 문제가 지속되면 관리자에게 연락해 주세요.</h1>", 404

@app.route('/')
def login():
    return render_template('login.html')


@app.route('/join')
def join():
    email_address = request.args.get("email_address")
    inputpw = request.args.get("inputpw")
    return render_template('variable.html',email_address=email_address,inputpw=inputpw)
       
@app.route('/loop')
def loop():
    value_list = ['list1','list2','list3']
    return render_template('loop.html',values=value_list)

@app.route('/numinput')
def numinput():
    return render_template('num.html')

@app.route('/if')
def if_test():
    number = int(request.args.get('number_input'))
    return render_template('if.html',value = number)



@app.route('/test', methods=['GET','POST','PUT','DELETE'])
def test():
    if request.method == 'POST':
        print('POST')
        data = request.get_json()
        print(data['email'])
    if request.method == 'GET':
        print('GET')
        user = request.args.get('email')
        print(user)
    if request.method == 'PUT':
        print('PUT')
        user = request.args.get('email')
        print(user)
    if request.method == 'PUT':
        print('PUT')
        user = request.args.get('email')
        print(user)

    return make_response(jsonify({'status':True}),200)

if __name__ == '__main__':
    app.run(host='localhost',port='8082',debug=False)

