from app import app, db
from flask import render_template, flash, redirect, request, json, jsonify, abort
from sqlmodel import event, eventSchema
from datetime import datetime, date

@app.route('/', methods = ['GET'])
def home():
    return render_template('base.html')

@app.route('/eventtrap/api/v1.0/events', methods=['POST'])
def create_event():
    if not request.json or not 'title' or not 'computer' in request.json:
        abort(400)
    e = event(title = request.json['title'],
              computer = request.json['computer'])
    if 'category' in request.json:
        e.category = request.json['category']
    db.session.add(e)
    db.session.commit()
    return jsonify({'status': 'ok'}), 201

@app.route('/eventtrap/api/v1.0/events', methods=['GET'])
def get_events():
    events = event.query.all()
    events_schema = eventSchema(many=True)
    result = events_schema.dump(events)        
    return jsonify(result)

@app.route('/eventtrap/api/v1.0/events/today', methods=['GET'])
def get_events_today():
    events = event.query.filter(event.date == date.today()).all()
    events_schema = eventSchema(many=True)
    result = events_schema.dump(events)        
    return jsonify(result)