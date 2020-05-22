# Envirophat Plant Monitor

A lightweight plant monitor server for [Pimoroni's EnviroPhat](https://github.com/pimoroni/enviro-phat), written in Django.

## Before you start
- Install the Envirophat dependencies using [Pimoroni's Envirophat installation guide](https://github.com/pimoroni/enviro-phat)
- Install [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

## Installation
```
# Clone the repository
git clone git@github.com:AlanCunningham/envirophat-plant-monitor.git

# Create a python virtual environment
virtualenv -system-site-packages -p python3 venv

# Activate the virtual environment
source venv/bin/activate

# Install the python dependencies using the requirements.txt file provided
pip install -r requirements

# Create a cronjob to get data from the envirophat sensor once an hour
crontab -e
# m h  dom mon dow  command
  0 *   *   *   *   {path to virtualenv}/bin/python {path to project}/manage.py get_sensor_data
```

## Run the server
```
python manage.py runserver 0:8000
```
The server will be available at http://localhost:8000/monitor/graph
