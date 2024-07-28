# Price Alert API

This is a Price Alert API that allows users to set alerts for cryptocurrency prices. The application will notify users via email when the price of a specific cryptocurrency reaches their target value.

## Features

- User registration and login
- Create, delete, and retrieve price alerts
- Real-time price monitoring using WebSockets
- Email notifications for price alerts

### Base URL

The base URL for the application is [https://tanxfitask.azurewebsites.net/](https://tanxfitask.azurewebsites.net/).

### API Documentation

The API documentation can be found at [https://documenter.getpostman.com/view/31915650/2sA3kaByXC](https://documenter.getpostman.com/view/31915650/2sA3kaByXC).

>[!NOTE]
>Kindly make use of the deployed link and Postman API to make use of the service faster and efficiently. But in case you would like to setup the project locally, here are the steps to get started


## Getting Started

### Prerequisites

- Python 3.12
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

## Usage

### User Registration

Start by registering yourself using the API and by making a POST request to the endpoint given below

Endpoint: `POST /auth/register`

Payload:

```json
{
  "email": "user@example.com",
  "password": "your-password"
}
```

Following which, you should receive an email similar to the one displayed below

![Registration Confirmation Email](images/Registration%20Confirmation%20Mail.png)

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
  "target_price": 30000
}
```

### All other endpoints can be accessed from the Postman Documentation [here](https://documenter.getpostman.com/view/31915650/2sA3kaByXC)

>[!IMPORTANT]
>Except for [Login](https://documenter.getpostman.com/view/31915650/2sA3kaByXC#b86e230e-6792-4c08-8e9a-4b583437937c) or [Register](https://documenter.getpostman.com/view/31915650/2sA3kaByXC#0936f1c4-91ce-4c1f-927e-d74a7ff50d92), all other endpoints need token to be sent along with the request as a bearer to identify the user from the backend, at any point of time, to fetch the token, user can enter their credetentials under [Login](https://documenter.getpostman.com/view/31915650/2sA3kaByXC#b86e230e-6792-4c08-8e9a-4b583437937c) endpoint to receive token as a response.

### Given below is a screenshot of the email received when the price reaches the desired amount

![Price Alert Email](images/Price%20Alert.png)

## Authors

- Sai Sahith Bonugala - Vellore Institute of Technology (21BIT0175)
