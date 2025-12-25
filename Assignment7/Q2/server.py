from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/soil_moisture_reading')
def create_soil_moisture_readings():
    sensor_id = request.form.get('sensor_id')
    moisture_level = request.form.get('moisture_level')
    date_time = request.form.get('date_time')

    query = f"insert into soil_moisture_readings values('{sensor_id}', {moisture_level},  '{date_time}');"

    executeQuery(query=query)

    return "soil_moisture_readings is added successfully"

@server.get('/soil_moisture_reading')
def retrieve_soil_moisture_readings():
    query = "select * from soil_moisture_readings;"

    data = executeSelectQuery(query=query)

    return f"soil_moisture_readings : {data}"

@server.put('/soil_moisture_reading')
def update_soil_moisture_readings():
    sensor_id = request.form.get('sensor_id')
    moisture_level = request.form.get('moisture_level')

    query = f"update soil_moisture_readings SET moisture_level = '{moisture_level}' where sensor_id = '{sensor_id}';"

    executeQuery(query=query)

    return "moisture_level is updated successfully"

@server.delete('/soil_moisture_reading')
def delete_soil_moisture_readings():
    sensor_id = request.form.get('sensor_id')

    query = f"delete from soil_moisture_readings where sensor_id = '{sensor_id}';"

    executeQuery(query=query)

    return "soil_moisture_readings is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=5000, debug=True)