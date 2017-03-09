# CUED Part IA Flood Warning System

This is the Part IA Lent Term computing activity at the Department of
Engineering, University of Cambridge.

The activity is documented at and meets the deliverables described at
http://cued-partia-flood-warning.readthedocs.io/. 

In addition to what is documented there, a flask based RESTful server is included which can be used to access the data generated
via http. To use it, simply run "python3 app.py&", which will leave the server to run on the background and can be accessed
from http://localhost:5000/floodwarning/stationlist (or replace stationlist with risks). This will return a JSON object
containing all the basic information regarding the UK flood monitoring stations as well as risks calculated by the floodwarning api as described in the project deliverables. 

The testing files in this project implement a library called hypothesis, which will be required for pytest to work and ensures
that everything is working as intended by generating random test data and keeping a history of past problems to continue checking.
