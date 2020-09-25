import os

from flask import Flask

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config = True)
	app.config.from_mapping(SECRET_KEY = "dev", DATABASE = os.path.join(app.instance_path, "flaskr.sqlite"))
	if test_config is None:
		app.config.from_pyfile("config.py", silent = True)
	else:
		app.config.from_pyfile(test_config)
	
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass
	
	from . import db
	db.init_app(app)

	from . import home
	app.register_blueprint(home.bp)

	from . import search
	app.register_blueprint(search.bp)

	from . import create
	app.register_blueprint(create.bp)

	app.add_url_rule("/", endpoint = "home.index")

	return app

