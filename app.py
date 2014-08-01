from pychumil import get_brightest_hyg, gt_lat, gt_lon
import datetime
from flask import Flask, jsonify, make_response, request
from flask_cors import cross_origin
import json
from bson import json_util
import logging

from flask.ext.cache import Cache   

lat = gt_lat
lon = gt_lon
gtm = -6

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
app.cache = Cache(app)   

@app.route("/brightest_hyg")
@app.cache.cached(timeout=300)  # cache this view for 5 minutes
@cross_origin()
def cached_stars():
    now = datetime.datetime.utcnow()
    resp = make_response(
      json.dumps({
        'stars': get_brightest_hyg(lat, lon), 
        'utcnow': now,
        'lat': lat,
        'lon': lon
      },  default=json_util.default)
    )
    return resp

if __name__ == "__main__":
    app.run(port=1024, debug=True, host='0.0.0.0')
