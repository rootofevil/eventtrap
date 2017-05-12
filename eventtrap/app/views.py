from app import app, db
from flask import render_template, flash, redirect, request, jsonify, abort
from sqlmodel import event

@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/eventtrap/api/v1.0/events', methods=['POST'])
def create_task():
    if not request.json or not 'title' or not 'computer' in request.json:
        abort(400)
    e = event(title = request.json['title'],
              computer = request.json['computer'])
    if 'category' in request.json:
        e.category = request.json['category']
    db.session.add(e)
    db.session.commit()
    return jsonify({'status': 'ok'}), 201