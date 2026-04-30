from car import Car
from truck import Truck
from motorcycle import Motorcycle
from file_handler import save_fleet_to_file, load_fleet_from_file

if __name__ == "__main__":

    vehicles = [
        Car("V001", "Tesla Model 3", 2023, "Electric", 4),
        Truck("T101", "Volvo FH16", 2019, 25000, 6),
        Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport"),
        Car("V002", "Toyota Corolla", 2018, "Petrol", 4),
        Truck("T102", "Mercedes Actros", 2021, 18000, 4),
        Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")
    ]


    save_fleet_to_file(vehicles, "fleet.txt")


    print("Loading fleet data from 'fleet.txt'...")
    loaded_vehicles = load_fleet_from_file("fleet.txt")
    print(f"{len(loaded_vehicles)} vehicles loaded successfully.")


    print(" --- All Vehicles ---")
    for vehicle in loaded_vehicles:
        print(f" {vehicle}")


    print(" --- Recent Vehicles (Last 4 Years) ---")
    recent_vehicles = [v for v in loaded_vehicles if v.is_new(4)]
    for vehicle in recent_vehicles:
        print(f" {vehicle}")

    print(" --- Electric Cars Only ---")
    electric_cars = [v for v in loaded_vehicles if isinstance(v, Car) and v.fuel_type == "Electric"]
    for car in electric_cars:
        print(f" {car}")