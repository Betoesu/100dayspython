from flask import Flask

def make_bold(func):
    def wrapper_function():
        return "<b>" + func() + "</b>"
    return wrapper_function

def make_italic(func):
    def wrapper_function():
        return "<em>" + func() + "</em>"
    return wrapper_function

def make_underline(func):
    def wrapper_function():
        return "<u>" + func() + "</u>"
    return wrapper_function

def make_paragraph(func):
    def wrapper_function():
        return "<u>" + func() + "</u>"
    return wrapper_function

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
    '<p>This is a paragraph.</p>' \
    '<img src="https://media.tenor.com/7pHHq-0cWzgAAAAM/champagne-and.gif" width=500>'


@app.route("/bye")
@make_bold
@make_italic
@make_underline
def say_bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"<h1>Hello there {name}, you are {number} years old"

if __name__ == "__main__":
    app.run(debug=True)