import requests
url = "https://api.citybik.es/v2/networks/citi-bike-nyc"
response = requests.get(url)
data = response.json()
name = data["network"]["name"]
city = data["network"]["location"]["city"]
country = data["network"]["location"]["country"]
print("Network name:")
print(name)
print("City name:")
print(city)
print("Country name:")
print(country)
#Extra credit:
inputstat = input("Type in a station to see stats ->  ")
stations = data["network"]["stations"]
found = False
for station in stations:
    if station["name"] == inputstat:
        free = station["free_bikes"]
        empty = station["empty_slots"]
        print("Free bikes:")
        print(free)
        print("Empty slots:")
        print(empty)
        found = True
        break
if found == False:
    print("No station with that name found.")
