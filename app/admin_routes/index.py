# -*- encoding=utf-8 -*-
from app import app
from flask import Flask
from flask import render_template
from flask import Blueprint

main = Blueprint('index', __name__)



@main.route('/')
def index():
    return render_template('home/index.html ')
