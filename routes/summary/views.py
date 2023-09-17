from datetime import datetime
from flask import Blueprint, jsonify, request
from extensions import db
from routes.journal.models import Mood
from routes.summary.services import generate_summary

blueprint = Blueprint("summary", __name__, url_prefix='/summary')

@blueprint.route("/")
def hello():
    print(type(db))
    return "Hello World!"


@blueprint.route("/<int:uid>/get", methods=['GET'])
def get_summary(uid):
    # Retrive arguments from request
    args = request.args
    start_date, end_date = args.get('start_date'), args.get('end_date')

    start_date = datetime(2023, 9, 10)
    end_date = datetime(2023, 9, 16)

    res = Mood.query.filter(Mood.date.between(start_date, end_date)).all()
    # extract relevant values
    res = [(mood.date, mood.is_day, mood.score) for mood in res]
    res = generate_summary(res)
    return jsonify(res)