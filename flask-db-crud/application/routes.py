from application import app, db
from application.models import Elves
from application.forms import TaskForm
from flask import render_template, request, redirect, url_for

@app.route('/')
def home():
    all_elves = Elves.query.all() 
    return render_template("index.html", title="Home", all_elves=all_elves)

@app.route('/create_elf')
def add():
    new_elf = Elves(name="New Elf")
    db.session.add(new_elf)
    db.session.commit()
    return "Added new elf to database"


@app.route('/read')
def read():
    all_elves = Elves.query.all()
    elves_string = ""
    for elf in all_elves:
        elves_string += "<br>"+ elf.name
    return elves_string

@app.route('/update/<name>')
def update(name):
    first_elf = Elves.query.first()
    first_elf.name = name
    db.session.commit()
    return first_elf.name