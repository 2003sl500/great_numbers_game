from flask import Flask, render_template, redirect, request, session
from random import random

app = Flask(__name__)
app.secret_key = "393920182830272984"

@app.route('/')
def index():
    if 'play_again' not in session:
        session['play_again'] = "Submit"
        
    if 'random_num' not in session:
        session['display_status'] = "none"
        session['random_num'] = (int)((random() * 100) + 1)

    return render_template('/index.html')

@app.route('/process', methods = ['POST'])
def submit():
    print('Submitted form')
    print(request.form['guess'])
    session['guess'] = request.form['guess']
    if (int)(session['guess']) == (int)(session['random_num']):
        session['answer_output'] = f"{session['guess']} was the number!"
        session.pop('random_num')
        session['play_again'] = "Play Again"
        session['display_status'] = "none"
    elif (int)(session['guess']) < (int)(session['random_num']):
        session['answer_output'] = f"{session['guess']} was too low"
        session['play_again'] = "Submit"
        session['color'] = "green"
        session['display_status'] = "block"
    else:
        session['answer_output'] = f"{session['guess']} was too high"
        session['play_again'] = "Submit"
        session['color'] = "red"
        session['display_status'] = "block"

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)