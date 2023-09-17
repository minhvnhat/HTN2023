from flask import Blueprint, request, jsonify, abort
from extensions import db
from sqlalchemy import text
from .models import Journal, Mood
from . schema import JournalResponse

from datetime import datetime

blueprint = Blueprint("journal", __name__, url_prefix='/journal')

@blueprint.route("/")
def hello():
    print(type(db))
    return "Hello World!"


@blueprint.route("/<int:uid>/send", methods=['POST'])
def send_journal(uid):
    data = request.get_json()
    prompt = data.get('prompt')
    msg = data.get('msg')

    print(prompt, msg)

    current_datetime = datetime.now()

    db.session.add(Journal(
        uid=uid,
        date=current_datetime, 
        prompt=prompt, 
        message=msg))
    db.session.commit()

    return f"Received POST request with uid: {uid} and msg: {msg}"


@blueprint.route("/<int:uid>/get", methods=['GET'])
def get_journals(uid):
    # Retrive arguments from request
    args = request.args
    start_date, end_date = args.get('start_date'), args.get('end_date')

    date_format = "%Y-%m-%d"

    # Use datetime.strptime() to parse the string into a datetime object
    start_date = datetime.strptime(start_date, date_format)
    end_date = datetime.strptime(end_date, date_format)

    res = Journal.query.filter_by(uid=uid).filter(Journal.date.between(start_date, end_date)).all()
    
    return jsonify(res)


@blueprint.route("/<int:uid>/send_mood", methods=['POST'])
def send_mood(uid):
    data = request.get_json()
    score = data.get('score')
    is_day = data.get('is_day')

    current_datetime = datetime.now()

    db.session.add(Mood(
        uid=uid,
        date=current_datetime, 
        score=score, 
        is_day=is_day))
    
    db.session.commit()

    return f"Received POST request with uid: {uid} and score: {score}"


@blueprint.route("/<int:uid>/get_mood", methods=['GET'])
def get_mood(uid):
    # Retrive arguments from request
    args = request.args
    start_date, end_date = args.get('start_date'), args.get('end_date')

    date_format = "%Y-%m-%d"

    # Use datetime.strptime() to parse the string into a datetime object
    start_date = datetime.strptime(start_date, date_format)
    end_date = datetime.strptime(end_date, date_format)

    res = Mood.query.filter_by(uid=uid).filter(Mood.date.between(start_date, end_date)).all()
    
    return jsonify(res)


@blueprint.route("/populate", methods=['GET'])
def populate():
    uid = 1
    data = [
        (10, 2, 1), (10, 3, 0), 
        (11, 4, 1), (11, 4, 0),
        (12, 1, 1), (12, 5, 0),
        (13, 5, 1), (13, 3, 0),
        (14, 2, 1), (14, 3, 0),
        (15, 5, 1), (15, 4, 0),
    ]

    for mood in data:
        db.session.add(Mood(
            uid=uid,
            date=datetime(2023, 9, mood[0]), 
            score=mood[1], 
            is_day=mood[2]))
    
    db.session.commit()

    return "Populated"

