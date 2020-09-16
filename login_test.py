from flask import Flask,jsonify,request,render_template

app = Flask(__name__,static_url_path='/static')

@app.route('/join')
def join():
    email_address = request.args.get("email_address")
    inputpw = request.args.get("inputpw")

    if email_address == "tpdnd7890@gmail.com" and inputpw == "qkrtpdnd123@":
        approach = {"authr" : "success"}
    else:
        approach = {"authr" : "fail"}
    return jsonify(approach)
       
@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)