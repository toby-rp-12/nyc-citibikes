# CS-api-project
My first API project.

## Overview

For my first API python code, I decided to make a program that will print the real-time statistics about any Citi Bike station in the NYC areas. I enjoyed getting to make this project.

This project is a Python program that fetches real-time data from the Citi Bike public API and displays information about the bike network, including its name, city, and country. It also allows users to look up statistics for individual bike stations.

The program uses the **CityBikes API** to:
- Retrieve live Citi Bike network data
- Display basic network information
- Allow users to search for a station by name
- Show how many bikes are available and how many docks are empty at that station

This project demonstrates how to work with APIs, JSON data, and user input in Python. The project is intended for educational use.

## Key Features

- Fetches live data from a public API
- Uses the `requests` library to make HTTP requests
- Parses nested JSON data
- Displays network name, city, and country
- Allows station lookup by name
- Shows available bikes and empty slots
- Handles invalid station names gracefully

## API Used

- **CityBikes API**
- Endpoint used:
https://api.citybik.es/v2/networks/citi-bike-nyc


The API provides live data about bike-sharing networks and stations.

## Example Output
```
Network name:
Citi Bike
City name:
New York
Country name:
US
Type in a station to see stats 
-> W 52 St & 11 Ave
Free bikes:
7
Empty slots:
32
```

If the station is not found:
```
No station with that name found.
```
