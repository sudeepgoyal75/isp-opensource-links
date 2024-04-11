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

# Time step (30 minutes)
step = timedelta(minutes=30)

# Initialize an empty list to store data points
data_points = []

# Planets and celestial points to track
bodies = ['jupiter', 'moon', 'mercury', 'venus', 'sun', 'saturn', 'rahu', 'ketu']

# Loop through each date and time and calculate the positions
ts = eph.timescale()
while start_date <= end_date:
    t = ts.utc(start_date)
    for body_name in bodies:
        body = eph[body_name]
        astrometric = (body + delhi).at(t)
        ra, dec, distance = astrometric.radec()
        
        # Prepare data point in InfluxDB line protocol format
        data_point = {
            "measurement": f"{body_name}_position",
            "time": start_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
            "fields": {
                "ra": ra._degrees,
                "dec": dec.degrees,
                "distance": distance.au
            }
        }
        data_points.append(data_point)
    
    # Move to the next time step
    start_date += step

# Write data to InfluxDB
client.write_points(data_points)

print("Data has been successfully written to InfluxDB.")
