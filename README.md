# LogMonitor
A prototype application to request and display logs from different servers

Required Modules
Flask
unittest
requests
PySide

Contents
Data - Test Data
core - Some core functionality
testing - Unit Tets
service - Service for app servers (servers on which the logs have to be monitored) and master server
frontend - simple UI for demo purpose
docs - some basic documentation

To execute

open Terminal 
cd to srvice folder
python loggerapp.py

open Terminal
cd to service folder
python masterapp.py

open Terminal
cd to frontend folder
python logChecker.py

Note python version used3.9.6
On Mac python should be replaced by python3
