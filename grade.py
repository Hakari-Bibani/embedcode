import folium
from geopy.distance import geodesic

def calculate_distances(points):
    """Calculate distances between all points."""
    dist_1_2 = geodesic(points[0], points[1]).kilometers
    dist_2_3 = geodesic(points[1], points[2]).kilometers
    dist_1_3 = geodesic(points[0], points[2]).kilometers
    return dist_1_2, dist_2_3, dist_1_3

def create_map(points):
    """Create a folium map with the given points."""
    # Calculate map center
    center_lat = sum(p[0] for p in points) / len(points)
    center_lon = sum(p[1] for p in points) / len(points)
    
    # Create base map
    m = folium.Map(location=[center_lat, center_lon], zoom_start=10)
    
    # Add markers for each point
    colors = ['red', 'blue', 'green']
    for i, (point, color) in enumerate(zip(points, colors), 1):
        folium.Marker(
            point,
            popup=f'Point {i}',
            icon=folium.Icon(color=color, icon='info-sign')
        ).add_to(m)
    
    # Add connecting lines
    folium.PolyLine(
        points + [points[0]],  # Connect back to first point
        weight=2,
        color='purple',
        opacity=0.8
    ).add_to(m)
    
    return m

def grade_submission(code):
    """Grade the submitted code based on defined criteria."""
    points = 0
    
    # 1. Code Structure and Implementation (30 points)
    # Check required library imports (5 points)
    required_libraries = ['folium', 'geopy', 'geodesic']
    for lib in required_libraries:
        if lib in code:
            points += 1.67
    
    # Check coordinate handling (5 points)
    coordinates = [
        '36.325735', '43.928414',
        '36.393432', '44.586781',
        '36.660477', '43.840174'
    ]
    for coord in coordinates:
        if coord in code:
            points += 0.83
    
    # Code execution (10 points)
    try:
        exec(code)
        points += 10
        
        # Code efficiency (10 points)
        if 'def' in code:  # Function definition exists
            points += 5
        if code.count('for') <= 2:  # Efficient loops
            points += 5
    except:
        pass
    
    # 2. Map Visualization (40 points)
    if 'folium.Map' in code:
        points += 15  # Base map creation
    
    if 'Marker' in code and 'add_to' in code:
        points += 15  # Point markers
    
    if 'PolyLine' in code:
        points += 10  # Connecting lines
    
    # 3. Distance Calculations (30 points)
    if 'geodesic' in code:
        points += 10  # Using geodesic distance
    
    # Check distance accuracy (20 points)
    reference_distances = [59.57, 73.14, 37.98]
    for dist in reference_distances:
        if str(round(dist, 2)) in code:
            points += 6.67
    
    return round(points)
