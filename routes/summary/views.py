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

    date_format = "%Y-%m-%d"

    # Use datetime.strptime() to parse the string into a datetime object
    start_date = datetime.strptime(start_date, date_format)
    end_date = datetime.strptime(end_date, date_format)

    res = Mood.query.filter_by(uid=uid).filter(Mood.date.between(start_date, end_date)).all()
    # extract relevant values
    res = [(mood.date, mood.is_day, mood.score) for mood in res]
    res = generate_summary(res)
    return jsonify(res)