from ipaddress import ip_address
import ipaddress
import socket
from turtle import color
import geocoder
import folium

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name Is: " + hostname)
print("Your Computer IP Address Is: " + IPAddr)

ip = geocoder.ip("me")
print(ip.address)
print(ip.latlng)

location = ip.latlng

map = folium.Map(location=location, zoom_start=10)
folium.CircleMarker(location=location, radius=50, color="red").add_to(map)
folium.Marker(location).add_to(map)

map

map.save("map.html")