# from 02_flask_template_lab.models.events_list import add_new_event
from flask import render_template, request, redirect
from app import *
from models.event_list import events, add_new_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['POST'])
def add_event():

    event_date = request.form['event_date']
    event_name = request.form['event_name']
    guest_total = request.form['guest_total']
    room_location = request.form['room_location']
    event_description = request.form['event_description']
    
    new_event = Event(event_date, event_name, guest_total, room_location, event_description, False)
    add_new_event(new_event)
    return redirect('/events')

