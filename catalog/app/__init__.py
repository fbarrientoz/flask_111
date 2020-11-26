#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Module init file"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

from app import routes

