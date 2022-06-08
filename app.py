from flask import Flask,render_template,request,jsonify
import re
app = Flask(__name__)

@app.get("/")
def index():
    return  render_template("form.html")


def checkUser(username):
    # check kung si username must contain number and lowercase charaacter and with the min 8 and max 18
    if re.search("^(?=.*[a-z])(?=.*\d)[a-z\d]{8,18}$",username):
        return True
    else:
        return False

def checkPassword(password):
    # check kung si password must contain number and lowercase and uppercase charaacter ,symbol and
    #  with the min 8 and max 18 length
    if re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$",password):
        return True
    else:
        return False

@app.post("/validation")
def process():
    email = request.form['email']
    username  = request.form["username"]
    password = request.form["password"]
    if checkUser(username) and checkPassword(password):
        return jsonify({'message':True})
    else:
        return jsonify({'message':False})


if __name__== "__main__":
    app.run(debug=True)