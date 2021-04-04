from flask import render_template, request, redirect, url_for, flash

from app import app, db
from .forms import UserForm, LookupForm, JackpotForm
from .models import User

import random

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/jackpot', methods=['POST', 'GET'])
def jackpot():
    jackpot_form = JackpotForm()
    
    if request.method == 'POST':
        if jackpot_form.validate_on_submit():
            # Get validated data from form
            phone_number = jackpot_form.phone_number.data  # You could also have used request.form['email']
            jackpot_keys = jackpot_form.jackpot_keys.data
            user = User.query.filter_by(phone_number=phone_number).first()
            jackpot = User.query.filter_by(phone_number=phone_number, jackpot_keys=jackpot_keys).first()
            
            if user:
                flash('User found')
                if jackpot:
                    return render_template('jackpot.html', title = "CONGRATULATION!!! YOU HIT THE JACKPOT!!!")
                else:
                    return render_template('jackpot.html', title = "SORRY!!! YOU MISS THE JACKPOT")
            else:
                flash("No match candidate's phone number!")
                return render_template('jackpot.html',form=jackpot_form, title="JACKPOT", flag=1)
    
    flash_errors(jackpot_form)   

    return render_template('jackpot.html', form=jackpot_form, flag=1, title="JACKPOT")

@app.route('/register', methods=['POST', 'GET'])
def register():
    user_form = UserForm()
    if request.method == 'POST':
        if user_form.validate_on_submit():
            # Get validated data from form
            name = user_form.name.data  # You could also have used request.form['name']
            phone_number = user_form.phone_number.data  # You could also have used request.form['email']
            image = user_form.image.data
            
            def get_random_number():
                return random.randrange(1000,9999)
            
            jackpot_keys = get_random_number()
            # save user to database
            user = User(name, phone_number, image, jackpot_keys)
            db.session.add(user)
            db.session.commit()

            flash('User successfully added')
            return redirect(url_for('register'))
    
    flash_errors(user_form)   
    return render_template('register.html', form = user_form)

@app.route('/lookup', methods=['POST', 'GET'])
def lookup():
    lookup_form = LookupForm()
    if request.method == 'POST':
        if lookup_form.validate_on_submit():
            # Get validated data from form
            phone_number = lookup_form.phone_number.data  # You could also have used request.form['email']
            user = User.query.filter_by(phone_number=phone_number).first()
            
            if user:
                # save user to database
                # res = User(user.name, user.phone_number, image, jackpot_keys)

                flash('User found')
                
                return render_template('lookup.html', match=user)
    
    flash_errors(lookup_form)   
    return render_template('lookup.html', form = lookup_form)

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
