## embedded SQL in Python
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
from flask import abort, render_template, Flask
import logging
import db

APP = Flask(__name__)

# Start page
@APP.route('/')
def index():
    stats = {}
    stats = db.execute('''
    SELECT * FROM
      (SELECT COUNT(*) n_movies FROM MOVIE)
    JOIN
      (SELECT COUNT(*) n_actors FROM ACTOR)
    JOIN
      (SELECT COUNT(*) n_genres FROM MOVIE_GENRE)
    JOIN 
      (SELECT COUNT(*) n_streams FROM STREAM)
    JOIN 
      (SELECT COUNT(*) n_customers FROM CUSTOMER)
    JOIN 
      (SELECT COUNT(*) n_countries FROM COUNTRY)
    JOIN 
      (SELECT COUNT(*) n_regions FROM REGION)
    JOIN 
      (SELECT COUNT(*) n_staff FROM STAFF)
    ''').fetchone()
    logging.info(stats)
    return render_template('index.html',stats=stats)
