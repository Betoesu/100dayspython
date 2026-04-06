from flask import Flask
import random





random_number = random.randint(0,20)
print(random_number)

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 20</h1>' \
           '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExejhhN3NncmQ4ZmxjeWtvc3l6aWFnczF3aWZwazkzdzFiamozYXF3MCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/eyTXyVqx9lHdWT3gJ7/giphy.gif">'

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnNoYXZ1bDRnMWFwYTVlNnFtOTBzdmhlYjM0Ynp3eHZrNWsybzI3ZCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/9G9Vd4iRDWym49JnWO/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3hkdDk0YXA1YWloZWI0ampyNjFsb3Z2eXRudWN6NDg5enc2ajYwdyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/jnAP1hq3Vr2vADLWtx/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You achieve to be a true Warrior!</h1>" \
               "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2hpd20wamxscmQxdnk2YmZxbzRueDhybGRkZGt2ZmFsM24xNGcwMyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/19NxXhWqsc7KLbzCJ6/giphy.gif'/>"

if __name__ == "__main__":
    app.run(debug=True)