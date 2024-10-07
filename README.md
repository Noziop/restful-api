# Basic API Security Implementation

## Description

This project implements a simple Flask-based API with basic security features, focusing on authentication and authorization. It's part of a larger exercise on RESTful API development and security practices.

## Features

- Basic HTTP Authentication
- JWT (JSON Web Token) Authentication
- Role-based access control
- Secure password hashing
- Protected routes for different authentication methods

## Technologies Used

- Python 3.x
- Flask
- Flask-HTTPAuth
- Flask-JWT-Extended
- Werkzeug

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Noziop/restful-api.git
```


2. Navigate to the project directory:

```bash
cd restful-api
```


3. Install the required dependencies:

```bash
pip install flask flask-httpauth flask-jwt-extended werkzeug
```


## Usage

1. Start the Flask server:

```bash
python task_05_basic_security.py
```


2. The API will be available at `http://localhost:5000`

## API Endpoints

- `GET /basic-protected`: Route protected by Basic Authentication
- `POST /login`: Endpoint to obtain JWT token
- `GET /jwt-protected`: Route protected by JWT Authentication
- `GET /admin-only`: Admin-only route (requires JWT with admin role)

## Authentication

- Basic Authentication: Use username and password for `/basic-protected`
- JWT Authentication: 
1. Obtain token via `/login` endpoint
2. Use token for accessing `/jwt-protected` and `/admin-only` routes

## Testing

You can test the API using curl or any API testing tool. Example commands:

```bash
# Basic Auth
curl -u user1:password http://localhost:5000/basic-protected

# Obtain JWT Token
curl -X POST -H "Content-Type: application/json" -d '{"username":"user1","password":"password"}' http://localhost:5000/login

# Access JWT protected route
curl -H "Authorization: Bearer <your_jwt_token>" http://localhost:5000/jwt-protected

# Access admin-only route (requires admin token)
curl -H "Authorization: Bearer <admin_jwt_token>" http://localhost:5000/admin-only
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.