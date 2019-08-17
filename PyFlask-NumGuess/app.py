"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.

The number Guesser is a copy of Charlie Smith's video here:
https://www.youtube.com/watch?v=NkguagDgrak
"""

from flask import Flask, render_template, request
import random
app = Flask(__name__)
global comp_num, counter  #globals can cause problems, hence the forced declaration
counter = 0
comp_num = random.randint(1,10)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/', methods = ['GET', 'POST']) #both GET and POST are necessary in upper case
def guess():
    global comp_num, counter # continuation of work around for globals
    message = ""
    if request.method == "POST": #must be upper case POST
        counter += 1
        form = request.form
        user_guess = int(form["guess"])
        if comp_num == user_guess:
            message = "Well done, you got it!"
            return render_template("game_over.html", message = message)
        elif comp_num > user_guess:
            message = "Too low"
        else:
            message = "Too high"
        if counter == 4:
            message = "You failed"            
            return render_template("game_over.html", message = message)
    return render_template("guess.html", message = message)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug = True)
