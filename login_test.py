from flask import Flask,jsonify,request,render_template,make_response
from flask_cors import CORS
import requests

app = Flask(__name__,static_url_path='/static')
CORS(app)

@app.errorhandler(404) #없는 페이지 요청했을 때 에러
def page_not_found(error):
    return "<h1>404 Error</h1>", 404

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
    app.run(host='localhost',port='8082',debug=True)

