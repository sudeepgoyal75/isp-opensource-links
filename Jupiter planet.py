from skyfield.api import load, Topos
from influxdb import InfluxDBClient
from datetime import datetime, timedelta

# Connect to InfluxDB
client = InfluxDBClient(host='localhost', port=8086, username='your_username', password='your_password', database='your_database')

# Load ephemeris data
eph = load('de421.bsp')

# Delhi's latitude and longitude
delhi = Topos(latitude=28.7041, longitude=77.1025)

# Start and end date for the data
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

# Time step (1 day)
step = timedelta(days=1)

# Initialize an empty list to store data points
data_points = []

# Loop through each date and calculate the position of Jupiter
ts = eph.timescale()
while start_date <= end_date:
    t = ts.utc(start_date)
    planet = eph['jupiter']
    astrometric = (planet + delhi).at(t)
    ra, dec, distance = astrometric.radec()
    
    # Prepare data point in InfluxDB line protocol format
    data_point = {
        "measurement": "jupiter_position",
        "time": start_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "fields": {
            "ra": ra._degrees,
            "dec": dec.degrees,
            "distance": distance.au
        }
    }
    data_points.append(data_point)
    
    # Move to the next day
    start_date += step

# Write data to InfluxDB
client.write_points(data_points)

print("Data has been successfully written to InfluxDB.")
