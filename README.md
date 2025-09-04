# rainfall_psql_flask_template
## Flask app that sorts/selects/limits/graphs rainfall data from postgres database


Installation notes:

clone repo to a designated directory on your computer (i.e. in a terminal cd to where you want it)
<p>
  download .zip file into your project directory


The data directory contains raw rainfall data and sql scripts to configure table and insert data
<p>Files contained in data directory:<p>
   1. psql_Create_Rainfall_Table.sql<p>      
   2. psql_Create_Rainfall_Table2.sql<p>
   3. njrainfall.txt<p>
   4. rainfall_month.txt<p>

## cd to the data dir:
Make sure the postgres.app is running on your machine
## In a terminal/shell window type
## sudo -u postgres psql to start the postgres.app as postgres user
'psql' to start the postgres.app

## from psql prompt type
CREATE DATABASE rainfall;

## Connect to the president database
\c rainfall

## To create the rainfall tables, enter
\i psql_Create_Rainfall_Table.sql
\i psql_Create_Rainfall_Table2.sql


Remove all records from table
DELETE from rainfall_table;
DELETE from rainfall_month;
## populate table directly from text file
\COPY rainfall_table FROM 'njrainfall.txt' with DELIMITER E' ';
\COPY rainfall_month FROM 'rainfall_month.txt' with DELIMITER E' ';
###E escapes the following character (ie tab delimited format)

\q to quit

## In the rainfall_psql directory  (cd to main_app directory)
## Edit the app.config line in get_rainfall.py to reflect your local address to the database

*****************************************
 Connect to your local postgres database
*****************************************

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:your_login_name@localhost/rainfall'


## create a new virtual environment in the rainfall_flask_postgres_template directory
python3 -m venv venv

## activate the virtual environment
source venv/bin/activate

## if you want to deactivate when your finished<p>
type deactivate to exit virtual enviro


## initialize git for this directory
git init

## install any required packages for this app
## may need to deactivate virtual machine after installing Flask 3.1.2
## pip3 install package_name==X.Y.Z to install manually
pip3 install -r requirements.txt

## USE the start.sh script in the rainfall_psql directory to start the app
## in terminal type (if error: permission denied: ./start.sh then try again after chmod +x ./start.sh to grant permission)
./start.sh

## in your browser
## go to the localhost address to access database
http://127.0.0.1:5000/

type control c in terminal window to quit

# Working Example of this application can be found at

https://get-pres.herokuapp.com/
