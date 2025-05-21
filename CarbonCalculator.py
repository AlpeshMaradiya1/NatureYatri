# List of major Indian cities
cities = [
    "Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore", "Hyderabad", "Ahmedabad", "Pune", "Jaipur", "Lucknow",
    "Surat", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Patna", "Vadodara", "Ghaziabad",
    "Ludhiana", "Agra", "Nashik", "Faridabad", "Meerut", "Rajkot", "Varanasi", "Srinagar", "Aurangabad", "Dhanbad"
]

# Predefined distances between cities (in km) - approximate values
city_distances = {
    ("delhi", "mumbai"): 1400.0, ("delhi", "kolkata"): 1500.0, ("delhi", "chennai"): 2200.0, ("delhi", "bangalore"): 2100.0,
    ("delhi", "hyderabad"): 1500.0, ("delhi", "ahmedabad"): 900.0, ("delhi", "pune"): 1400.0, ("delhi", "jaipur"): 300.0,
    ("delhi", "lucknow"): 500.0, ("delhi", "surat"): 1185.0, ("delhi", "kanpur"): 400.0, ("delhi", "nagpur"): 1000.0,
    ("delhi", "indore"): 800.0, ("delhi", "thane"): 1400.0, ("delhi", "bhopal"): 750.0, ("delhi", "visakhapatnam"): 1700.0,
    ("delhi", "patna"): 1000.0, ("delhi", "vadodara"): 1000.0, ("delhi", "ghaziabad"): 20.0, ("delhi", "ludhiana"): 300.0,
    ("delhi", "agra"): 200.0, ("delhi", "nashik"): 1100.0, ("delhi", "faridabad"): 30.0, ("delhi", "meerut"): 70.0,
    ("delhi", "rajkot"): 1100.0, ("delhi", "varanasi"): 800.0, ("delhi", "srinagar"): 800.0, ("delhi", "aurangabad"): 1200.0,
    ("delhi", "dhanbad"): 1100.0,
    ("mumbai", "kolkata"): 1900.0, ("mumbai", "chennai"): 1300.0, ("mumbai", "bangalore"): 1000.0, ("mumbai", "hyderabad"): 700.0,
    ("mumbai", "ahmedabad"): 500.0, ("mumbai", "pune"): 150.0, ("mumbai", "jaipur"): 1100.0, ("mumbai", "lucknow"): 1400.0,
    ("mumbai", "surat"): 300.0, ("mumbai", "kanpur"): 1200.0, ("mumbai", "nagpur"): 800.0, ("mumbai", "indore"): 600.0,
    ("mumbai", "thane"): 20.0, ("mumbai", "bhopal"): 750.0, ("mumbai", "visakhapatnam"): 1300.0, ("mumbai", "patna"): 1700.0,
    ("mumbai", "vadodara"): 400.0, ("mumbai", "ghaziabad"): 1400.0, ("mumbai", "ludhiana"): 1600.0, ("mumbai", "agra"): 1200.0,
    ("mumbai", "nashik"): 150.0, ("mumbai", "faridabad"): 1400.0, ("mumbai", "meerut"): 1500.0, ("mumbai", "rajkot"): 700.0,
    ("mumbai", "varanasi"): 1500.0, ("mumbai", "srinagar"): 2000.0, ("mumbai", "aurangabad"): 350.0, ("mumbai", "dhanbad"): 1800.0,
    ("kolkata", "chennai"): 1700.0, ("kolkata", "bangalore"): 1900.0, ("kolkata", "hyderabad"): 1500.0, ("kolkata", "ahmedabad"): 2000.0,
    ("kolkata", "pune"): 1800.0, ("kolkata", "jaipur"): 1500.0, ("kolkata", "lucknow"): 1000.0, ("kolkata", "surat"): 1800.0,
    ("kolkata", "kanpur"): 1000.0, ("kolkata", "nagpur"): 1100.0, ("kolkata", "indore"): 1400.0, ("kolkata", "thane"): 1900.0,
    ("kolkata", "bhopal"): 1300.0, ("kolkata", "visakhapatnam"): 800.0, ("kolkata", "patna"): 600.0, ("kolkata", "vadodara"): 1800.0,
    ("kolkata", "ghaziabad"): 1500.0, ("kolkata", "ludhiana"): 1700.0, ("kolkata", "agra"): 1200.0, ("kolkata", "nashik"): 1700.0,
    ("kolkata", "faridabad"): 1500.0, ("kolkata", "meerut"): 1600.0, ("kolkata", "rajkot"): 2100.0, ("kolkata", "varanasi"): 700.0,
    ("kolkata", "srinagar"): 2000.0, ("kolkata", "aurangabad"): 1600.0, ("kolkata", "dhanbad"): 300.0,
    ("chennai", "bangalore"): 350.0, ("chennai", "hyderabad"): 600.0, ("chennai", "ahmedabad"): 1700.0, ("chennai", "pune"): 1100.0,
    ("chennai", "jaipur"): 2200.0, ("chennai", "lucknow"): 2000.0, ("chennai", "surat"): 1500.0, ("chennai", "kanpur"): 1900.0,
    ("chennai", "nagpur"): 1100.0, ("chennai", "indore"): 1400.0, ("chennai", "thane"): 1300.0, ("chennai", "bhopal"): 1500.0,
    ("chennai", "visakhapatnam"): 800.0, ("chennai", "patna"): 1900.0, ("chennai", "vadodara"): 1500.0, ("chennai", "ghaziabad"): 2200.0,
    ("chennai", "ludhiana"): 2400.0, ("chennai", "agra"): 2000.0, ("chennai", "nashik"): 1200.0, ("chennai", "faridabad"): 2200.0,
    ("chennai", "meerut"): 2300.0, ("chennai", "rajkot"): 1800.0, ("chennai", "varanasi"): 1900.0, ("chennai", "srinagar"): 2700.0,
    ("chennai", "aurangabad"): 1100.0, ("chennai", "dhanbad"): 1700.0,
    ("bangalore", "hyderabad"): 550.0, ("bangalore", "ahmedabad"): 1400.0, ("bangalore", "pune"): 850.0, ("bangalore", "jaipur"): 2000.0,
    ("bangalore", "lucknow"): 1800.0, ("bangalore", "surat"): 1100.0, ("bangalore", "kanpur"): 1800.0, ("bangalore", "nagpur"): 900.0,
    ("bangalore", "indore"): 1200.0, ("bangalore", "thane"): 1000.0, ("bangalore", "bhopal"): 1400.0, ("bangalore", "visakhapatnam"): 1000.0,
    ("bangalore", "patna"): 2000.0, ("bangalore", "vadodara"): 1300.0, ("bangalore", "ghaziabad"): 2100.0, ("bangalore", "ludhiana"): 2300.0,
    ("bangalore", "agra"): 1900.0, ("bangalore", "nashik"): 900.0, ("bangalore", "faridabad"): 2100.0, ("bangalore", "meerut"): 2200.0,
    ("bangalore", "rajkot"): 1500.0, ("bangalore", "varanasi"): 1800.0, ("bangalore", "srinagar"): 2600.0, ("bangalore", "aurangabad"): 900.0,
    ("bangalore", "dhanbad"): 1900.0,
}

# Emission factors (kg CO₂ per km per person) - approximate values
emission_factors = {
    "Walking": 0.0,
    "Cycling": 0.0,
    "Metro": 0.04,    # Efficient public transport
    "Train": 0.06,    # Indian Railways average
    "EV Car": 0.08,   # Electric vehicle with India's grid mix
    "Bus": 0.1,       # Diesel/CNG bus average
    "Bike": 0.12,     # Petrol-powered two-wheeler
    "Car (CNG)": 0.16, # CNG car
    "Car (Petrol)": 0.2, # Petrol car
    "Flight": 0.25,   # Domestic flight average
}

def search_cities(search_term):
    search_term = search_term.lower()
    return [city for city in cities if search_term in city.lower()]

def calculate_emissions(origin, destination):
    origin, destination = origin.lower(), destination.lower()
    
    city_pair = (origin, destination)
    reverse_pair = (destination, origin)
    if city_pair in city_distances:
        distance = city_distances[city_pair]
    elif reverse_pair in city_distances:
        distance = city_distances[reverse_pair]
    else:
        return "Distance between these cities is not available in the database.", None

    emissions = {}
    for mode, factor in emission_factors.items():
        if mode in ["Walking", "Cycling"] and distance > 10:
            emissions[mode] = "Not practical for this distance"
        else:
            emission = distance * factor
            emissions[mode] = round(emission, 2)

    result = f"Distance between {origin.capitalize()} and {destination.capitalize()}: {distance} km\n"
    result += "Carbon Emissions by Transportation Mode:\n"
    for mode, emission in emissions.items():
        if isinstance(emission, str):
            result += f"{mode}: {emission}\n"
        else:
            result += f"{mode}: {emission} kg CO₂\n"
    
    return result, distance

# Interactive calculator loop with question-answer format
if __name__ == "__main__":
    print("Welcome to the Carbon Emission Calculator for Indian Cities!")
    print("Answer the questions below to calculate the distance and emissions between two cities.")
    print("Available cities (you can search for a city by typing a partial name):")
    print(", ".join(cities))
    
    while True:
        # Question 1: Origin city
        while True:
            search_term = input("\nQuestion 1: What is your origin city? (or type 'list' to see all cities, 'exit' to quit): ").strip()
            if search_term.lower() == "exit":
                print("Exiting the calculator. Goodbye!")
                exit()
            if search_term.lower() == "list":
                print(", ".join(cities))
                continue
            matching_cities = search_cities(search_term)
            if not matching_cities:
                print("No matching cities found. Please try again.")
            elif len(matching_cities) == 1:
                origin = matching_cities[0]
                break
            else:
                print("Matching cities:", ", ".join(matching_cities))
                origin = input("Please select a city from the list: ").strip()
                if origin in matching_cities:
                    break
                else:
                    print("Invalid selection. Please try again.")

        # Question 2: Destination city
        while True:
            search_term = input("\nQuestion 2: What is your destination city? (or type 'list' to see all cities, 'exit' to quit): ").strip()
            if search_term.lower() == "exit":
                print("Exiting the calculator. Goodbye!")
                exit()
            if search_term.lower() == "list":
                print(", ".join(cities))
                continue
            matching_cities = search_cities(search_term)
            if not matching_cities:
                print("No matching cities found. Please try again.")
            elif len(matching_cities) == 1:
                destination = matching_cities[0]
                break
            else:
                print("Matching cities:", ", ".join(matching_cities))
                destination = input("Please select a city from the list: ").strip()
                if destination in matching_cities:
                    break
                else:
                    print("Invalid selection. Please try again.")

        # Calculate and display results
        if not origin or not destination:
            print("Error: City names cannot be empty.")
        else:
            result, distance = calculate_emissions(origin, destination)
            print("\nResults:")
            print(result)

        # Question 3: Calculate another route?
        while True:
            again = input("\nQuestion 3: Do you want to calculate emissions for another route? (yes/no): ").strip().lower()
            if again in ["yes", "no"]:
                break
            print("Please enter 'yes' or 'no'.")
        if again != "yes":
            print("Exiting the calculator. Goodbye!")
            break