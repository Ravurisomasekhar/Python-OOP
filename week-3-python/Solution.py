# itinerary_item.py
class ItineraryItem:
    def __init__(self, description, type, dateTime, location, details):
        self.description = description
        self.type = type
        self.dateTime = dateTime
        self.location = location
        self.details = details
        
    def display_details(self):
        return f"description: {self.description}, type: {self.type}, dateTime: {self.dateTime}, location: {self.location}, details:{self.details}"    
    # Todo

# trip.py
class Trip:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
        # Todo
    
    def remove_item(self, identifier):
        for i in self.items:
            # print(i)
            if i.description in identifier:
                self.items.remove(i)
                return True 
        return False    
        # Todo
    
    def get_items(self):
        return self.items        
        # Todo
    
    def filter_items(self, criteria, value):
        lst = []
        if criteria == "description":
            for i in self.items:
                if i.description  == value:
                    lst.append(i)
            return lst
        
        if criteria == "type":
            for i in self.items:
                if i.type  == value:
                    lst.append(i)
            return lst    
        
        if criteria == "dateTime":
            for i in self.items:
                if i.dateTime  == value:
                    lst.append(i)
            return lst 
        
        if criteria == "location":
            for i in self.items:
                if i.location  == value:
                    lst.append(i)
            return lst 
        
        if criteria == "details":
            for i in self.items:
                if i.details  == value:
                    lst.append(i)
            return lst  
        # Todo
    
    def search_items(self, keyword):
        # keyword = "Eiffel"
        lst = []
        for i in self.items:
            if (keyword.lower() in i.description.lower()):
                lst.append(i)
            elif (keyword.lower() in i.type.lower()):
                lst.append(i)  
            elif (keyword.lower() in i.dateTime.lower()):
                lst.append(i)   
            elif (keyword.lower() in i.location.lower()):
                lst.append(i)
            elif (keyword.lower() in i.details.lower()):
                lst.append(i)
        return lst               
        # Todo

# travel_manager.py
class TravelManager:
    def __init__(self):
        self.trips = []
    
    def create_trip(self, name):
        self.trips.append(Trip(name))
        # Todo
    
    def delete_trip(self, name):
        for i in self.trips:
            if i.name == name:
                self.trips.remove(i)
                return True
        return False    
        # Todo
    
    def get_trip(self, name):
        for i in self.trips:
            if i.name == name:
                return i 
        # Todo
    
    def list_trips(self):
        return  self.trips
        # Todo
    
    def cross_trip_search(self, keyword):
        lst = []
        for i in self.trips:
            j = i.search_items(keyword)
            lst.extend(j)
        return lst    
        # Todo

