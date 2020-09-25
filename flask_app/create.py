from flask import (
        Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask_app.db import get_db
bp = Blueprint("create", __name__, url_prefix = "/create")

@bp.route("/create", methods = ("GET", ))
def create():
	return render_template("create/index.html", error = None)

@bp.route("/create_group", methods = ("GET", "POST"))
def create_group():
	error = None;
	if request.method == "POST":
		db = get_db()
		name = request.form["name"]
		description = request.form["description"]

		if name == "":
			error = "Please enter a name for the group."
		elif db.execute("SELECT name FROM elo_group WHERE name = ?", (name, )).fetchone() is not None:
			error = "A group named \"{}\" has already been created.".format(name)

		if error is None:
			db.execute("INSERT INTO elo_group (name, description) VALUES (?, ?)", (name, description))
			db.commit()
			return redirect(url_for("home.index"))
		flash(error)
	return render_template("create/index.html", error = error)

