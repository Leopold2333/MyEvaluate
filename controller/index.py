from flask import Blueprint, render_template, session, request, redirect, url_for


index = Blueprint('index', __name__)


@index.route('/')
def home():

    return render_template('evaluate.html', login=session.get('username'))


