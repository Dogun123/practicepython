from flask import Flask,jsonify,request,render_template,make_response
from flask_cors import CORS

app = Flask(__name__,static_url_path='/static')
CORS(app)


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

@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify(success=True),200)

if __name__ == '__main__':
    app.run(debug=True)