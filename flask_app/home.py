from flask import (
        Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask_app.db import get_db

bp = Blueprint("home", __name__, url_prefix = "/index")

@bp.route("/", methods = ("GET",))
def index():
	return render_template("index.html")

