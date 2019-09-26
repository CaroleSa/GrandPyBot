web: gunicorn program:app
init: FLASK_APP=run.py flask init_db