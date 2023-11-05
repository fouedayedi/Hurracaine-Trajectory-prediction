import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the Haversine distance between two points on the Earth.

    Parameters:
    - lat1, lon1: Latitude and longitude of the first point.
    - lat2, lon2: Latitude and longitude of the second point.

    Returns:
    - Distance between the two points in kilometers.
    """
    
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Radius of the Earth in kilometers
    R = 6371.0
    distance = R * c
    
    return distance

def travel_angle(lat1, lon1, lat2, lon2):
    """
    Calculate the angle of travel between two points on the Earth.

    Parameters:
    - lat1, lon1: Latitude and longitude of the first point.
    - lat2, lon2: Latitude and longitude of the second point.

    Returns:
    - Angle of travel in degrees, where North is 0 degrees and angles increase clockwise.
    """
    
    # Calculate the differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Calculate the angle in radians using the arctangent of the differences
    angle_rad = math.atan2(dlon, dlat)
    
    # Convert the angle from radians to degrees
    angle_deg = math.degrees(angle_rad)
    
    # Ensure the angle is within [0, 360] range
    angle_deg = (angle_deg + 360) % 360
    
    return angle_deg

# Example usage:
# distance = haversine_distance(40.7128, -74.0060, 34.0522, -118.2437)
# angle = travel_angle(40.7128, -74.0060, 34.0522, -118.2437)

def extract_travel_parameters(lats, lons):
    """
    Extract the total distances and angles of travel for a sequence of latitude and longitude points.
    
    Parameters:
    - lats: Series of latitudes.
    - lons: Series of longitudes.

    Returns:
    - List of distances traveled and list of angles of travel.
    """
    total_distances = [0]  # Starting point, so distance is 0
    angles = [None]        # No angle for the starting point

    for i in range(1, len(lats)):
        lat1, lon1 = lats.iloc[i-1], lons.iloc[i-1]
        lat2, lon2 = lats.iloc[i], lons.iloc[i]
        
        # Calculate distance
        distance = haversine_distance(lat1, lon1, lat2, lon2)
        total_distances.append(distance)
        
        # Calculate angle
        angle = travel_angle(lat1, lon1, lat2, lon2)
        angles.append(angle)

    return total_distances, angles