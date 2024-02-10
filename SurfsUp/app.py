# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt

# Python SQL toolkit and ORM
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
# >>Define what to do when a user hits the Homepage route<<
@app.route("/")
def welcome():
    return (
        f"Welcome to my homepage!<br>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>" 
        f"/api/v1.0/start/end"
    )

# >>Define what to do when a user hits each available route<<
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'precipitation'...")
     #1. Create our session (link) from Python to the DB
    session = Session(engine)

    #2. Query last 12 months of data from precipitation analysis 
    one_year = session.query(Measurement.date,Measurement.prcp).\
                filter(Measurement.date >= '2016-08-23').all()

    session.close()

    #3. Create a dictionary using 'date' as the key and 'prcp' as the value, and append to a list 
    one_year_list = []
    for date, prcp in one_year:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        one_year_list.append(precipitation_dict)

    #4. Return a JSON representation of dictionary
    return jsonify(one_year_list)
    
#--------------------------------------------------------------#
@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'stations'...")
    #1. Create our session (link) from Python to the DB
    session = Session(engine)

    #2. Query all stations
    all_stations = session.query(Station.station).all()

    session.close()

    #3. Convert list of tuples into normal list
    stations_list = list(np.ravel(all_stations))

    #4. Return a JSON list of stations
    return jsonify(stations_list)

#--------------------------------------------------------------#
@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'tobs'...")
    #1. Create our session (link) from Python to the DB
    session = Session(engine)

    #2. Query dates and temperature observations of most-active station for the previous year
    active_station = session.query(Measurement.date,Measurement.tobs).\
                    filter(Measurement.date >= '2016-08-23').\
                    filter(Measurement.station == 'USC00519281').\
                    order_by(Measurement.date).all()
    session.close()

    #3. Create a dictionary and append to a list
    tobs_list = []
    for date, tobs in active_station:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_list.append(tobs_dict)

    #4. Return a JSON list of temperature observations for the previous year
    return jsonify(tobs_list)

#--------------------------------------------------------------#
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature(start=None,end=None):
    print("Server received request for 'temperature'...in DATE FORMAT 'yyyy-mm-dd'")

    #1. Create our session (link) from Python to the DB
    session = Session(engine)

    if end==None: 
        #2. Calculate TMIN, TAVG, and TMAX for all dates greater than or equal to start date
        temperature_start = session.query(func.min(Measurement.tobs), 
                            func.avg(Measurement.tobs),
                            func.max(Measurement.tobs)).\
                            filter(Measurement.date >= start).all()
        
        #3. Convert list of tuples into normal list
        temperature_list = list(np.ravel(temperature_start))
    
        #4. Return a JSON list of minimum, average, maximum temperature for a specified start
        return jsonify(temperature_list)

    else: 
        #5. Calculate TMIN, TAVG, and TMAX for the dates from start date to end date 
        temperature_start_end = session.query(func.min(Measurement.tobs), 
                            func.avg(Measurement.tobs),
                            func.max(Measurement.tobs)).\
                            filter(Measurement.date >= start).filter(Measurement.date <= end).all()
        
        #6. Convert list of tuples into normal list
        temperature_end_list = list(np.ravel(temperature_start_end))

        #7. Return a JSON list of minimum, average, maximum temperature from start date to end date                         
        return jsonify(temperature_end_list)

    #8. Close the session
    session.close()

#--------------------------------------------------------------#    
# End main
if __name__ == "__main__":
    app.run(debug=True)





