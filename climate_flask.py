import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

from collections import defaultdict

# Database Setup
# ---------------------------------------------------
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


# Flask Setup
# ----------------------------------------------------
app = Flask(__name__)


# Flask Routes
# ----------------------------------------------------

@app.route("/")
def launch_page():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/Stations<br/>"
        f"/api/v1.0/Precipitation<br/>"
        f"/api/v1.0/Tobs<br/>"
        f"/api/v1.0/Start<br/>"
        f"/api/v1.0/Start-End"
    )


# Stations Route --------------------------------------

@app.route("/api/v1.0/Stations")
def station_names():
    # Create sesion from Python to Hawaii database
    session = Session(engine)

    # Query all stations from station table
    results = session.query(Station.station).all()
    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))
    return jsonify(all_names)


# Precipitation Route ---------------------------------

@app.route("/api/v1.0/Precipitation")
def precip_measure():
    # Create  session from Python to Hawaii database
    session = Session(engine)

    # Query daily rainfall and station location from measurement table; limit to last year
    results = session.query(Measurement.date, Measurement.prcp).\
        order_by(Measurement.date).\
        filter(Measurement.date >= "2016-08-24").all()

    session.close()

    # Create a list of dates (key values), with each date a list of temperatures for that date
    formatted_results = defaultdict(list)

    for date, prcp in results:
        formatted_results[date].append(prcp)

    return jsonify(formatted_results)


# Tobs Route -------------------------------------------

@app.route("/api/v1.0/Tobs")
def temps():
    # Create  session from Python to Hawaii database
    session = Session(engine)

    # Query daily rainfall and station location from measurement table; limit to last year and most active station
    results = session.query(Measurement.date, Measurement.prcp).\
        order_by(Measurement.date).\
        filter(Measurement.station == "USC00519397").\
        filter(Measurement.date >= "2016-08-24").all()

    session.close()

    return jsonify(results)


# Start Route -------------------------------------------

@app.route("/api/v1.0/Start")
def temps_start():
    # Create  session from Python to Hawaii database
    session = Session(engine)

    # Define start date (on or after 2016-08-24; must be in YYYY-MM-DD format)
    start_date = "2010-01-01"

    # Query daily rainfall and calculate min, avg, and max values for period
    low_temp = session.query(func.min(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    avg_temp = session.query(func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    hi_temp = session.query(func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    session.close()

    # Clean results and format output
    low_temp = list(np.ravel(low_temp))
    avg_temp = list(np.ravel(avg_temp))
    hi_temp = list(np.ravel(hi_temp))

    results = [{"Low Temp": low_temp}, {
        "Avg Temp": avg_temp}, {"High Temp": hi_temp}]

    return jsonify(results)


# Start / End Route --------------------------------------

@app.route("/api/v1.0/Start-End")
def temps_range():
    # Create  session from Python to Hawaii database
    session = Session(engine)

    # Define start date (on or after 2010-01-01 and on or before 2017-08-23; must be in YYYY-MM-DD format)
    start_date = "2016-01-01"
    end_date = "2017-08-23"

    # Query daily rainfall and calculate min, avg, and max values for period
    low_temp = session.query(func.min(Measurement.tobs)).\
        filter(Measurement.date >= start_date).\
        filter(Measurement.date <= end_date).all()
    avg_temp = session.query(func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start_date).\
        filter(Measurement.date <= end_date).all()
    hi_temp = session.query(func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).\
        filter(Measurement.date <= end_date).all()

    session.close()

    # Clean results and format output
    low_temp = list(np.ravel(low_temp))
    avg_temp = list(np.ravel(avg_temp))
    hi_temp = list(np.ravel(hi_temp))

    results = [{"Low Temp": low_temp}, {
        "Avg Temp": avg_temp}, {"High Temp": hi_temp}]

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
