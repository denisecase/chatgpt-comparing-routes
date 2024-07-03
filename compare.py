from geopy.distance import geodesic

# Coordinates for key points on the routes:
las_vegas = (36.1699, -115.1398)
reno = (39.5296, -119.8138)
ely = (39.2478, -114.8888)
fallon = (39.4756, -118.7774)
tonopah = (38.069, -117.2304)
hawthorne = (38.5244, -118.6223)
pahrump = (36.2083, -115.9839)
beatty = (36.9083, -116.7583)

# Route via US-95
route_us95 = [
    las_vegas,
    pahrump,
    beatty,
    tonopah,
    hawthorne,
    fallon,
    reno
]

# Route via US-93
route_us93 = [
    las_vegas,
    ely,
    fallon,
    reno
]

# Calculate total distances for each route
distance_us95 = sum([geodesic(route_us95[i], route_us95[i+1]).miles for i in range(len(route_us95)-1)])
distance_us93 = sum([geodesic(route_us93[i], route_us93[i+1]).miles for i in range(len(route_us93)-1)])

distance_us95, distance_us93
