# Enviro pHAT Plant Monitor

A lightweight plant monitor server for the [Pimoroni Enviro pHAT](https://github.com/pimoroni/enviro-phat), written in Django.

<img src="https://github.com/AlanCunningham/envirophat-plant-monitor/blob/master/readme_images/plant.jpg?raw=true" width="30%">  <img src="https://github.com/AlanCunningham/envirophat-plant-monitor/blob/master/readme_images/graph.png?raw=true" width="60%">


## Before you start
- Install the Envirophat dependencies using the [Pimoroni Enviro pHAT installation guide](https://github.com/pimoroni/enviro-phat)
- Install [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

## Installation
```
# Clone the repository
git clone git@github.com:AlanCunningham/envirophat-plant-monitor.git

# Create a python virtual environment
virtualenv --system-site-packages -p python3 venv

# Activate the virtual environment
source venv/bin/activate

# Install the python dependencies using the requirements.txt file provided
pip install -r requirements

# Create a cronjob to get data from the Enviro pHAT sensor once an hour
crontab -e
# m h  dom mon dow  command
  0 *   *   *   *   {path to virtualenv}/bin/python {path to project}/manage.py get_sensor_data
```

## Run the server
```
python manage.py runserver 0:8000
```
The server will be available at http://localhost:8000/monitor/graph
