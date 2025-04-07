
from Solution import ItineraryItem, Trip, TravelManager

def main():
    # Create itinerary items
    flight = ItineraryItem("Flight to Paris", "Flight", "2025-06-15 08:00", "Paris Charles de Gaulle", "Non-stop flight")
    hotel = ItineraryItem("Hotel Reservation", "Hotel", "2025-06-15 15:00", "Paris", "5-star hotel booking")
    activity = ItineraryItem("Eiffel Tower Visit", "Activity", "2025-06-16 10:00", "Paris", "Guided tour of the Eiffel Tower")
    
    # Test display_details for ItineraryItem
    if "Flight to Paris" in flight.display_details():
        print("ItineraryItem display_details test passed for flight.")
    else:
        print("ItineraryItem display_details test failed for flight.")
    
    # Create a Trip and add items
    trip = Trip("Paris Trip")
    trip.add_item(flight)
    trip.add_item(hotel)
    trip.add_item(activity)
    
    if len(trip.get_items()) == 3:
        print("Trip add_item test passed.")
    else:
        print("Trip add_item test failed.")
    
    # Test remove_item
    if trip.remove_item("Hotel Reservation") and len(trip.get_items()) == 2:
        print("Trip remove_item test passed.")
    else:
        print("Trip remove_item test failed.")
    
    # Edge case: remove non-existing item
    if not trip.remove_item("Non Existing Item"):
        print("Trip remove_item edge case test passed.")
    else:
        print("Trip remove_item edge case test failed.")
    
    # Test filter_items (filter by type "Flight")
    filtered = trip.filter_items("type", "Flight")
    if len(filtered) == 1 and filtered[0].type.lower() == "flight":
        print("Trip filter_items test passed.")
    else:
        print("Trip filter_items test failed.")
    
    # Test search_items (search for keyword "Eiffel")
    search_results = trip.search_items("Eiffel")
    if len(search_results) == 1 and "Eiffel Tower" in search_results[0].description:
        print("Trip search_items test passed.")
    else:
        print("Trip search_items test failed.")
    
    # Create a TravelManager and test trip management
    manager = TravelManager()
    manager.create_trip("Paris Trip")
    manager.create_trip("London Trip")
    
    if len(manager.list_trips()) == 2:
        print("TravelManager create_trip and list_trips test passed.")
    else:
        print("TravelManager create_trip and list_trips test failed.")
    
    # Test get_trip
    paris_trip = manager.get_trip("Paris Trip")
    if paris_trip is not None and paris_trip.name.lower() == "paris trip":
        print("TravelManager get_trip test passed.")
    else:
        print("TravelManager get_trip test failed.")
    
    # Test cross_trip_search
    london_trip = manager.get_trip("London Trip")
    london_activity = ItineraryItem("London Eye Visit", "Activity", "2025-07-20 12:00", "London", "Ride on the London Eye")
    london_trip.add_item(london_activity)

    eiffel_activity = ItineraryItem("Eiffel Eye visit", "Activity", "2025-07-20 12:00", "London", "Ride on the London Eye")
    london_trip.add_item(eiffel_activity)
    
    cross_search = manager.cross_trip_search("Visit")
    if len(cross_search) == 2:  # Should match "Eiffel Tower Visit" and "London Eye Visit"
        print("TravelManager cross_trip_search test passed.")
    else:
        print("TravelManager cross_trip_search test failed.")
    
    # Test delete_trip
    if manager.delete_trip("London Trip") and len(manager.list_trips()) == 1:
        print("TravelManager delete_trip test passed.")
    else:
        print("TravelManager delete_trip test failed.")
    
    # Edge case: delete non-existing trip
    if not manager.delete_trip("Non Existing Trip"):
        print("TravelManager delete_trip edge case test passed.")
    else:
        print("TravelManager delete_trip edge case test failed.")

main()
