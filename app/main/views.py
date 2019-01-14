# -*- coding:utf-8 -*-
__author__ = '东方鹗'

from flask import render_template, redirect, request, current_app, url_for, g
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('test.html')
