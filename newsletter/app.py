import os
from flask import Flask, render_template, session, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fd7as8fdsd0ffsd4wfwse'
    
    Bootstrap(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app

app = create_app()

db = SQLAlchemy(app)

class NewsletterForm(FlaskForm):
    ime = StringField(validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Pretplati se')

class Newsletter(db.Model):
    __tablename__ = 'newsletter'
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.Text())
    email = db.Column(db.Text(), unique=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    db.create_all()
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = NewsletterForm()

    if request.method == 'GET':
        return render_template('signup.html', form=form)

    elif request.method == 'POST' and form.validate_on_submit():
        ime = form.ime.data
        email = form.email.data

        temp = Newsletter(ime=form.ime.data, email=form.email.data)

        try:
            db.session.add(temp)
            db.session.commit()
            return redirect(url_for('ty', ime=ime))
        except exc.IntegrityError as e:
            db.session().rollback()
            flash('Već postoji korisnik s tim emailom!')
            return redirect(url_for('signup'))

    elif request.method == 'POST' and form.validate_on_submit() is False:
        flash('Email mora biti u pravilnom obliku!')
        return render_template('signup.html', form=form)
    

@app.route('/thank-you-<ime>', methods=['GET'])
def ty(ime):
    return render_template('registracija-zavrsena.html', ime=ime)