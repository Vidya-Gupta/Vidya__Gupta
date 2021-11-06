from flask import Flask,request, render_template
from flask.wrappers import Request
app = Flask(__name__)
app.config['SECRET_KEY'] = 'please_dont_hack_my_software-jhagdjasgd'
user_details={"vidya":"kpgi127", "user":"password","meera":"meera123"}


#@app.route("/")
#def homee():
#    return '<h1>Hello World</h1>'

##1
@app.route("/pizza")
def pizza():
    return '''<h1>There are many other interesting changes, please consult the "What's New" page in the documentation for a full list.</h1>'''

##2
@app.route("/home/<name>", methods = ["GET", "POST"])
def home(name):
    return "<h1>Hi {} you are on the home page. Welcome {} . You are from {} </h1>".format(name, "Biden", "US")

##3
@app.route("/query")
def query():
    name= request.args.get("name")
    location=request.args.get("location")
    return "<h1>Hi, My name is {} and i am from location {}. Now you are in the query page</h1>".format(name, location)

##4
@app.route("/")
def index():
    return render_template("index.html")

##5
@app.route("/art")
def art():
    return render_template("art.html")

##6
@app.route("/earth")
def earth():
    return render_template("earth.html")

##7
@app.route("/jupiter")
def jupiter():
    return render_template("jupiter.html")

##8
@app.route("/mars")
def mars():
    return render_template("mars.html")

##9
@app.route("/mercury")
def mercury():
    return render_template("mercury.html")

##10
@app.route("/myrecipefour")
def myrecipefour():
    return render_template("myrecipefour.html")

##11
@app.route("/myrecipeone")
def myrecipeone():
    return render_template("myrecipeone.html")

##12
@app.route("/myrecipethree")
def myrecipethree():
    return render_template("myrecipethree.html")

##13
@app.route("/myrecipetwo")
def myrecipetwo():
    return render_template("myrecipeteo.html")

##14
@app.route("/myschool")
def myschool():
    return render_template("myschool.html")

##15
@app.route("/neptune")
def neptune():
    return render_template("neptune.html")

##16
@app.route("/pluto")
def pluto():
    return render_template("pluto.html")

##17
@app.route("/recipebook")
def recipebook():
    return render_template("recipebook.html")

##18
@app.route("/saturn")
def saturn():
    return render_template("saturn.html")

##19
@app.route("/login")
def login():
        return render_template("login.html")


##20
@app.route("/solarsystem")
def solarsystem():
    return render_template("solarsystem.html")

##21
@app.route("/uranus")
def uranus ():
    return render_template("uranus.html")

##22
@app.route("/venus")
def venus():
    return render_template("venus.html")

##23
@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/user_validation", methods=['POST'])
def user_validation():
    username=request.form.get("userhtml")
    password=request.form.get("pwdhtml")
    returnval = login_success(user_details,username,password)
    if returnval == True:
        session["authenticated"] = True
        return render_template("loginsuccess.html", username = username)
    else:
        session["authenticated"] = False
        return render_template("loginfailure.html")

def login_success(dictionary, username, password):
    if dictionary.get(username, "User not found") == password:
        return True
    else:
        return False


##24
@app.route("/register_verify", methods=['POST'])
def register_verify():
    username = request.form.get("userhtml")
    password = request.form.get("pwdhtml")
    user_details[username] = password
    return render_template("register_verify.html")

##25
@app.route("/loginsuccess")
def loginsuccess():
    return render_template("loginsuccess.html")


def encrypt(message):
    encrypt = ''
    for m in message:
        a1 = ord(m)  #string is converted to number
        a2 = a1 + 5  #manupulating the string by adding some secret number
        a3 = chr(a2) #convert the number back to character
        encrypt = encrypt + a3
    return encrypt

#Decryption
#message1 = input("Enter a  message here to encrpt: ")
def decrypt(message1):
    decrypt = ''
    for n in message1:
        a4 = ord(n)
        a5 = a4 - 5
        a6 = chr(a5)
        decrypt = decrypt + a6
    return decrypt 

@app.route("/encrypt")
def encryption():
    return render_template("encrypt.html")

@app.route("/decrypt")
def decryption():
    return render_template("decrypt.html")

@app.route("/modify_encrypt", methods=['POST'])
def modify_encrypt():
    message = request.form.get("encrypt_html")
    enc_message = encrypt (message)
    return render_template ('encrypt.html', enc_m = enc_message)

@app.route("/modify_decrypt", methods=['POST'])
def modify_decrypt():
    message1 = request.form.get("decrypt_html")
    dec_message = decrypt (message1)
    return render_template ('decrypt.html', dec_m = dec_message)


@app.route('/calculator')
def calculator():
    return render_template("calculator.html")


def addition(num1,num2):
    sum = num1 + num2
    return sum

def subtraction(num1,num2):
    sub = num1 - num2
    return sub

def multiplication(num1, num2):
    mul_output = num1*num2
    return mul_output

def division(num1, num2):
    div_output = num1/num2
    return div_output

@app.route('/verify_calc', methods=['POST'])
def verify_calc():
    num1=request.form.get("number1")
    num2=request.form.get("number2")
    op=request.form.get("operator")
    # print(num1,num2,op)
    num1 = int(num1)
    num2 = int(num2)
    if op == "addition":
        result = addition(num1, num2)
    elif op == "subtraction":
        result = subtraction(num1,num2)
    elif op == "multiply":
        result = multiplication(num1,num2)
    elif op == "division":
        result = division(num1,num2)

    return render_template("verify_calc.html", result = result, num1 = num1, num2 = num2, op = op )



if __name__ == '__main__': 
    app.run(debug=True)
