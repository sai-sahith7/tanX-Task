# Price Alert API

This is a Price Alert API that allows users to set alerts for cryptocurrency prices. The application will notify users via email when the price of a specific cryptocurrency reaches their target value.

## Features

- User registration and login
- Create, delete, and retrieve price alerts
- Real-time price monitoring using WebSockets
- Email notifications for price alerts

## Project Structure

```
/app
├── Controllers
│   ├── alert.py
│   ├── auth.py
│   └── price.py
├── models
│   ├── alert.py
│   ├── log.py
│   └── user.py
├── routes
│   ├── alert.py
│   ├── auth.py
│   └── price.py
├── schemas
│   ├── alert.py
│   ├── token.py
│   └── user.py
├── utils
│   ├── db.py
│   ├── email.py
│   ├── hash.py
│   ├── jwt.py
│   └── websocket.py
└── main.py
.env
docker-compose.yaml
Dockerfile
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Create a `.env` file with the following content:

```
DB_HOST=<your-database-host>
DB_NAME=<your-database-name>
DB_USER=<your-database-user>
DB_PASSWORD=<your-database-password>
DB_PORT=<your-database-port>
SECRET_KEY=<your-secret-key>
SMTP_MAIL=<your-smtp-mail>
SMTP_PASSWORD=<your-smtp-password>
```

3. Build and run the application using Docker Compose:

```bash
docker-compose up --build
```

### API Documentation

The API documentation can be found [here](https://documenter.getpostman.com/view/31915650/2sA3kaByXC).

### Base URL

The base URL for the application is [https://tanxfitask.azurewebsites.net/](https://tanxfitask.azurewebsites.net/).

## Usage

### User Registration

Endpoint: `POST /auth/register`

Payload:

```json
{
  "email": "user@example.com",
  "password": "your-password"
}
```

### User Login

Endpoint: `POST /auth/login`

Payload:

```json
{
  "email": "user@example.com",
  "password": "your-password"
}
```

### Create Alert

Endpoint: `POST /alerts/create`

Payload:

```json
{
  "coin": "BTCUSDT",
  "target_price": 30000
}
```

### Delete Alert

Endpoint: `DELETE /alerts/delete`

Query Parameters:

- `id`: Alert ID

### Get Alerts

Endpoint: `GET /alerts`

Query Parameters:

- `skip`: Number of records to skip
- `limit`: Number of records to return
- `status`: Status of the alerts ("created", "triggered", "deleted")

## Screenshots

### Registration Confirmation Email

![Registration Confirmation Email](images/Registration%20Confirmation%20Mail.png)

### Price Alert Email

![Price Alert Email](images/Price%20Alert.png)

## Authors

- Sai Sahith Bonugala - Vellore Institute of Technology (21BIT0175)

## License

This project is licensed under the MIT License.
