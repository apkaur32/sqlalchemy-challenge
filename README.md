# sqlalchemy-challenge
Challenge#10 HW

Instructions: \ 
Congratulations! Treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with trip planning, one must do a climate analysis about the area. \ 

Part 1: Analyze and Explore the Climate Data \
In this section, use Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. Specifically, use SQLAlchemy ORM queries, Pandas, and Matplotlib and follow these steps: \
-Start with 'climate_starter.ipynb' and 'hawaii.sqlite' to complete climate analysis and data exploration. \
-Use the SQLAlchemy create_engine() function to connect to SQLite database. \
-Use the SQLAlchemy automap_base() function to reflect tables into classes, and then save references to the classes named 'station' and 'measurement'. \
-Link Python to the database by creating a SQLAlchemy session. \
-Perform a precipitation analysis and then a station analysis as outlines below. \
-Remember to close your session at the end of the notebook. \

Precipitation Analysis: \
1. Create a query that finds the most recent date in the dataset \
2. Create a query that collects only the date and prcp for the last year of data \
3. Save the query results to a Pandas DataFrame to create date and prcp columns \
4. Sort the DataFrame by date \
5. Plot the results with Matplotlib \
6. Use Pandas to print the summary statistics for the precipitation data \

Station Analysis: \ 
1. Design a query that finds the number of stations in the dataset  \
2. Design a query that lists the stations and observation counts in descending order and finds the most active station \
3. Design a query that finds the min, max, and average temperatures for the most active station \ 
4. Design a query to get the previous 12 months of temperature observation (TOBS) data that filters by the most active station \ 
5. Save the query results to a Pandas DataFrame  \
6. Plot a histogram with bins=12 for the last year of data using tobs as the column\

Part 2: Design Climate App with Flask API \
"/" Start at the homepage. List all the available routes. \
"/api/v1.0/precipitation" - Returns json with the date as the key and the value as precipitation for the last year \
"/api/v1.0/stations" - Returns jsonified data of all of the stations in the database \
"/api/v1.0/tobs" - Returns jsonified data for the most active station for the last year of data \
"/api/v1.0/<start>" - Inputs start date as a parameter and Returns the min, max, and average temperatures from start \
"/api/v1.0/<start>/<end>" - Inputs start and end dates as parameters and Returns the min, max, and average temperatures from start to end date \

In summary, this was a challenging assignment for which I reviewed class exercises, Stack Overflow, and worked with tutor, instructor during office hours, and practiced my SQL skills. 
