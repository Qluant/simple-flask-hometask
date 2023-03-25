from app import app
from flask import render_template, url_for, redirect
from app.website_processing import factor, operations
from random import randint


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/numbers")
def numbers():
    _list = [randint(1, 200) for x in range(15)]
    _list.sort()
    return render_template("numbers.html", numbers=_list)


@app.route("/profile")
def profile():
    person = {
        "Ім'я" : "Артем",
        "Вік" : 16,
        "Країна" : "Україна",
    }
    return render_template('profile.html', content = person)

    
@app.route("/factorial")
def factorial():       
    num = randint(0, 100)
    if num < 50:
        result = num * 1.5
    else:
        result = factor(count = num)
    return render_template("factorial.html", result=result)


@app.route("/calc/<int:number_1>&<operation>&<int:number_2>")
def calculator(number_1: int, operation: str, number_2: int):
    if operation not in operations:
        return redirect(url_for("index"))
    if operation == ':':
        operation = '/'
    result = eval(f"{number_1}{operation}{number_2}")
    return render_template("calculator.html", number_1=number_1, number_2=number_2, operation=operation, result=result)
