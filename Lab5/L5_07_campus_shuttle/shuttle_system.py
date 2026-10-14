"""Manage campus shuttle routes and trip records."""
import json
import random
from datetime import datetime
from pathlib import Path

# Global state
routes = {
    "R1": {"name": "Main Gate - Library", "trips": []},
    "R2": {"name": "Hostel - Sports Complex", "trips": []},
    "R3": {"name": "Admin Block - Metro", "trips": []},
}
MIN_CAPACITY = 10


def add_trip_log(route_id, passenger_count, logs=None):
    """Add a trip to the route and record it in the logs."""
    if route_id not in routes:
        raise ValueError(f"Unknown route: {route_id}")

    # Rejecting negative counts and values that are not integers.
    if (
        isinstance(passenger_count, bool)
        or not isinstance(passenger_count, int)
        or passenger_count < 0
    ):
        raise ValueError("Passenger count must be a non-negative integer.")

    # Avoiding to share the same default list between function calls.
    if logs is None:
        logs = []

    routes[route_id]["trips"].append(passenger_count)
    logs.append(
        f"{datetime.now().isoformat(timespec='seconds')}: "
        f"{route_id} carried {passenger_count}"
    )
    return logs


def remove_route(route_id):
    """Remove a route from the system."""
    if route_id not in routes:
        raise ValueError(f"Unknown route: {route_id}")
    del routes[route_id]


def average_load(route_id):
    """Calculate the average passenger count for a route."""
    if route_id not in routes:
        raise ValueError(f"Unknown route: {route_id}")

    trips = routes[route_id]["trips"]

    # Preventing division by zero when a route has no recorded trips.
    if not trips:
        return 0.0

    return sum(trips) / len(trips)


def underused_routes():
    """Find routes with an average load below capacity."""
    flagged = []

    # Checking recorded trips directly instead of hiding exceptions.
    for route_id, route in routes.items():
        if route["trips"] and average_load(route_id) < MIN_CAPACITY:
            flagged.append(route_id)

    return flagged


def assign_driver(route_id):
    """Assign a driver to a valid route."""
    # Validating the route before assigning a driver.
    if route_id not in routes:
        raise ValueError(f"Unknown route: {route_id}")

    drivers = ["Prakash", "Leela", "Imran", "Tom"]
    return random.choice(drivers)


def sync_fleet_data(file="fleet.json"):
    """Save the current route data to a JSON file."""
    Path(file).write_text(
        json.dumps(routes, indent=4),
        encoding="utf-8",
    )


def main():
    """Run the shuttle tracking program."""
    logs = []

    add_trip_log("R1", 32, logs)
    add_trip_log("R1", 28, logs)
    add_trip_log("R2", 4, logs)

    print("Trip logs:")
    for log in logs:
        print(log)

    print("Driver for R1:", assign_driver("R1"))
    print("Underused:", underused_routes())
    print("R1 average:", average_load("R1"))
    print("R3 average:", average_load("R3"))

    sync_fleet_data()

    choice = input("Route to look up (Enter for R2): ").strip().upper()
    if not choice:
        choice = "R2"

    if choice in routes:
        print("Trips on", choice, ":", routes[choice]["trips"])
    else:
        print("Unknown route. Available routes:", ", ".join(routes))


if __name__ == "__main__":
    main()
