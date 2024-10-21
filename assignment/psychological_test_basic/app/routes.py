from flask import Blueprint, jsonify, render_template, request, url_for
from .database import db
from .models import Participant,Answer
import pytz
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def home():
    # 참여자 정보 입력 페이지를 렌더링합니다.
    return render_template("index.html")


@main.route("/participants", methods=["POST"])
def add_participant():
    data=request.json
    new_participant=Participant(name = data["name"],age = data["age"],gender = data["gender"])
    db.session.add(new_participant)
    db.session.commit()
    return jsonify({"redirect":url_for("main.question"),"participant_id":new_participant.id})


@main.route("/question", methods=["get"])
def question():
    return render_template("question.html")


@main.route("/submit", methods=["POST"])
def submit():
    participant_id = request.cookies.get("participant_id")
    answers = request.json
    answers=answers.get("answers",None)
    for answer in answers:
        new_answer=Answer(question_id=answer["question_id"],choice=True if answer["chosen_answer"] == "yes" else False,participant_id=participant_id)
        db.session.add(new_answer)
        db.session.commit()
    return ""

