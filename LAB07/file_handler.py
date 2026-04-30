from car import Car
from truck import Truck
from motorcycle import Motorcycle

def save_fleet_to_file(vehicles, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for vehicle in vehicles:
            if isinstance(vehicle, Car):
                line = f"Car,{vehicle.vid},{vehicle.model},{vehicle.year},{vehicle.fuel_type},{vehicle.doors}\n"
            elif isinstance(vehicle, Truck):
                line = f"Truck,{vehicle.vid},{vehicle.model},{vehicle.year},{vehicle.max_load},{vehicle.axles}\n"
            elif isinstance(vehicle, Motorcycle):
                line = f"Motorcycle,{vehicle.vid},{vehicle.model},{vehicle.year},{vehicle.engine_cc},{vehicle.type}\n"
            file.write(line)
    print(f"Fleet saved to '{filename}'")


def load_fleet_from_file(filename):
    vehicles = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(',')
            vehicle_type = parts[0]

            if vehicle_type == "Car":
                vehicle = Car(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5]))
            elif vehicle_type == "Truck":
                vehicle = Truck(parts[1], parts[2], int(parts[3]), int(parts[4]), int(parts[5]))
            elif vehicle_type == "Motorcycle":
                vehicle = Motorcycle(parts[1], parts[2], int(parts[3]), int(parts[4]), parts[5])

            vehicles.append(vehicle)

    return vehicles