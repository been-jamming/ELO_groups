from flask import (
        Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask_app.db import get_db

bp = Blueprint("search", __name__, url_prefix = "/search")

@bp.route("/", methods = ("GET", ))
def search():
	db = get_db()
	results = db.execute("SELECT * FROM elo_group WHERE name LIKE :name ORDER BY LENGTH(name) - INSTR(name, REPLACE(:name, '%', ''))  LIMIT 20", ("%" + request.args.get("q") + "%",)).fetchall()
	return render_template("search/index.html", results = results, q=request.args.get("q"))
