import pandas as pd
import requests
import re
from datetime import datetime

API_KEY = "AIzaSyDVI_HLPb1lYJg7HnL69ilqGc4l1AkzmcY"

df = pd.read_csv("FinalV1.csv")

def time_to_minutes(time_str):
    """Converts a time string (HH:MM) to minutes."""
    if not isinstance(time_str, str) or time_str == 'NULL' or time_str is None:
        return 0  # Return 0 or some default value for invalid or missing times
    try:
        time_obj = datetime.strptime(time_str, "%H:%M")
        return time_obj.hour * 60 + time_obj.minute
    except ValueError:
        return 0  # Handle invalid time format gracefully

def time_optimization(recommended_places, current_time):
    """Optimize the time schedule based on available time."""
    optimized_schedule = []
    available_time = time_to_minutes(current_time)
    
    for place in recommended_places:
        open_time = time_to_minutes(place["open_1"])
        close_time = time_to_minutes(place["close_1"])
        
        # Assume 60 minutes (1 hour) as the average time spent at each place
        avg_time_spent = 60  # Fixed time spent (1 hour)

        # Check if the place can fit into the available time slot
        if available_time >= open_time and available_time + avg_time_spent <= close_time:
            optimized_schedule.append(place)
            available_time += avg_time_spent  # Update available time for the next place

    return optimized_schedule

def calculate_score(row, user_type, user_budget):
    """Calculate score for each place based on user preferences."""
    rating_score = row["google_ratings"] * 3
    cost_score = (
        0
        if row["avg_cost_per_person"] > user_budget
        else (user_budget - row["avg_cost_per_person"]) / user_budget * 10
    )
    rating_count_score = (row["number_of_ratings"] / 1000) * 3
    restaurant_bonus = 100 if row["type_of_place"] == "Food" else 0
    type_match_bonus = 200 if row["type_of_place"] == user_type else 0
    total_score = (
        rating_score
        + cost_score
        + rating_count_score
        + restaurant_bonus
        + type_match_bonus
    )
    return total_score

def recommend_places(user_type, user_budget):
    """Recommend places based on user input."""
    df["avg_cost_per_person"] = pd.to_numeric(
        df["avg_cost_per_person"], errors="coerce"
    )
    df["number_of_ratings"] = pd.to_numeric(df["number_of_ratings"], errors="coerce")
    df["score"] = df.apply(
        calculate_score, axis=1, user_type=user_type, user_budget=user_budget
    )
    recommended_places = df.sort_values(by="score", ascending=False)
    food_places = df[df["type_of_place"] == "Food"].sort_values(
        by="score", ascending=False
    )
    recommended_places = (
        pd.concat([recommended_places.head(3), food_places.head(2)]).drop_duplicates()
        .reset_index(drop=True)
    )
    return recommended_places[[
        "place_name", "score", "google_ratings", "number_of_ratings",
        "avg_cost_per_person", "type_of_place", "open_1", "close_1"
    ]]

def get_route_and_distance(origin, destination, api_key):
    """Fetch the route and distance between two places using Google Directions API."""
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "OK":
        legs = data["routes"][0]["legs"][0]
        distance_text = legs["distance"]["text"]
        distance_value = float(re.findall(r"\d+\.?\d*", distance_text)[0])
        duration = legs["duration"]["text"]
        return distance_value, duration
    else:
        print(f"Error fetching directions from {origin} to {destination}")
        return None, None

def generate_routes_and_distances(place_names, api_key):
    """Generate and print routes and distances between each pair of places."""
    distance_array = []
    travel_time_array = []
    for i in range(len(place_names) - 1):
        place1, place2 = place_names[i], place_names[i + 1]
        distance, duration = get_route_and_distance(place1, place2, api_key)
        if distance and duration:
            distance_array.append(distance)
            travel_time_array.append(duration)
    return distance_array, travel_time_array

def main():
    """Main program logic."""
    user_type = input("Enter the type of trip (e.g., Sightseeing, Food, Shopping): ")
    user_budget = float(input("Enter your budget per person: "))
    user_hotel_name = input("Which hotel are you staying in? ")
    current_time = input("Enter your current time (HH:MM): ")

    recommended = recommend_places(user_type, user_budget)
    top_places = (
        recommended[recommended["type_of_place"] == user_type]
        .head(3)["place_name"]
        .tolist()
    )
    top_restaurants = (
        recommended[recommended["type_of_place"] == "Food"]
        .head(2)["place_name"]
        .tolist()
        if user_type != "Food"
        else []
    )
    all_places = top_places + top_restaurants

    if user_hotel_name in all_places:
        all_places.remove(user_hotel_name)
        next_place = recommended[~recommended["place_name"].isin(all_places)].iloc[0][
            "place_name"
        ]
        all_places.append(next_place)

    all_places.insert(0, user_hotel_name)

    # Optimize schedule based on time
    optimized_schedule = time_optimization(
        recommended[recommended["place_name"].isin(all_places)].to_dict(orient="records"),
        current_time
    )

    # Generate distance matrix and calculate travel times between places
    distance_array, travel_time_array = generate_routes_and_distances(all_places, API_KEY)

    # Output the optimized route with distances and times
    total_distance = 0
    print(f"\nOptimized travel itinerary:")

    route_details = []

    current_time_in_minutes = time_to_minutes(current_time)
    last_place = user_hotel_name  # Track the last place visited
    for i, place in enumerate(optimized_schedule):
        arrival_time = current_time_in_minutes
        travel_time = travel_time_array[i] if i < len(travel_time_array) else "N/A"
        arrival_time_str = str(datetime.strptime(str(arrival_time // 60) + ":" + str(arrival_time % 60), "%H:%M").time())
        departure_time = str(datetime.strptime(str((arrival_time + 60) // 60) + ":" + str((arrival_time + 60) % 60), "%H:%M").time())
        
        # Output the current place and transition to next place
        route_details.append(f"{last_place} -> {place['place_name']} -> Arrival: {arrival_time_str}, Departure: {departure_time}, Travel Time: {travel_time}, Distance: {distance_array[i]} km")
        
        total_distance += distance_array[i]
        last_place = place['place_name']  # Update the last visited place
        current_time_in_minutes = arrival_time + 60  # Add 60 minutes after visiting a place

    # Closing the loop (returning to the starting place)
    distance, _ = get_route_and_distance(optimized_schedule[-1]["place_name"], user_hotel_name, API_KEY)
    route_details.append(f"{last_place} -> {user_hotel_name} -> Arrival: {arrival_time_str}, Departure: {departure_time}, Travel Time: {travel_time}, Distance: {distance} km")

    # Calculate total distance
    total_distance = round(total_distance + distance, 2)

    # Print route and final summary
    print(" -> ".join(route_details))
    print(f"\nTotal distance to cover: {total_distance} km")

if __name__ == "__main__":
    main()
