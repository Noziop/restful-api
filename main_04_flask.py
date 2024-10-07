#!/usr/bin/python3


import requests
import json


BASE_URL = "http://localhost:5000"


def test_api():
    # Test the home route
    response = requests.get(f"{BASE_URL}/")
    print("1. Testing home route:")
    print(f"   Response: {response.text}")
    print(f"   Status Code: {response.status_code}\n")

    # Test the data route
    response = requests.get(f"{BASE_URL}/data")
    print("2. Testing data route:")
    print(f"   Response: {response.json()}")
    print(f"   Status Code: {response.status_code}\n")

    # Test the status route
    response = requests.get(f"{BASE_URL}/status")
    print("3. Testing status route:")
    print(f"   Response: {response.text}")
    print(f"   Status Code: {response.status_code}\n")

    # Test getting an existing user
    response = requests.get(f"{BASE_URL}/users/jane")
    print("4. Testing get existing user:")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
    print(f"   Status Code: {response.status_code}\n")

    # Test getting a non-existing user
    response = requests.get(f"{BASE_URL}/users/nonexistent")
    print("5. Testing get non-existing user:")
    print(f"   Response: {response.json()}")
    print(f"   Status Code: {response.status_code}\n")

    # Test adding a new user
    new_user = {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }
    response = requests.post(f"{BASE_URL}/add_user", json=new_user)
    print("6. Testing add new user:")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
    print(f"   Status Code: {response.status_code}\n")

    # Verify the new user was added
    response = requests.get(f"{BASE_URL}/users/alice")
    print("7. Verifying new user was added:")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
    print(f"   Status Code: {response.status_code}\n")

    # Test adding a user with an existing username
    response = requests.post(f"{BASE_URL}/add_user", json=new_user)
    print("8. Testing add user with existing username:")
    print(f"   Response: {response.json()}")
    print(f"   Status Code: {response.status_code}\n")


if __name__ == "__main__":
    test_api()