from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)


@app.route('/homepage')
def homepage():
    words = story.prompts
    return render_template("homepage.html", words=words)

@app.route('/story')
def make_story():

    text = story.generate(request.args)

    return render_template('story.html', text=text)
