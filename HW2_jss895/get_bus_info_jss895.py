from __future__ import print_function
import pylab as pl
import os
import json
import pandas as pd

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


# the next import allows me to read line input arguments
import sys

if not len(sys.argv) == 4:
    print ("This is too much")

key=sys.argv[1]
bus=sys.argv[2]
csvfile=sys.argv[3]

print("your key is",key)
print("your bus is",bus)

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+ key + "&VehicleMonitoringDetailLevel=calls&LineRef="+ bus

print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

a=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print ("There are",(len(a)),"buses, and their locations are:")
print

#data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][1]["MonitoredVehicleJourney"]["VehicleLocation"]

df = pd.DataFrame()

for it in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
    Busname=(it["MonitoredVehicleJourney"]["VehicleRef"])
    Latitude=(it["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"])
    Longitude=(it["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"])
    StopName=(it["MonitoredVehicleJourney"]["MonitoredCall"]["StopPointName"])
    StopStatus=(it["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"])
    bus_things = [{'Busname': Busname, "Latitude": Latitude, "Longitude": Longitude, 'StopName': StopName, 'StopStatus': StopStatus}]
    df=df.append(bus_things)

df.StopName = df.StopName.replace("","N/A")
fout="queonda"
df.to_csv(fout+".csv", index=False)
print ("Your file has been saved to "+fout+".csv")
