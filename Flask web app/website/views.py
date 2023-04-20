from flask import Blueprint, render_template

#it's has a buch of roots inside of it.v it has a bunch of URLs definded in here.

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

