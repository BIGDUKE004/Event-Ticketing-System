# EventPad: Event Ticketing System (Backend)

This is the backend API for an event ticketing app. Organizers can create events and set up ticket types for them, and customers can book tickets and pay. It's written in Python with FastAPI and stores everything in MySQL.

I built it to practice designing a layered API (routers, services, repositories) and writing business logic that I can test without needing a database.

## What it does

- Sign up and log in. Passwords are hashed with Argon2 and logins return a JWT that expires after 30 minutes. A user is either a customer or an organizer.
- Create, view, search, update and delete events. Searching is by keyword.
- Add ticket types to an event (for example Regular or VIP), each with its own price and quantity. When a ticket type runs out, it's marked as sold out.
- Book tickets. A booking can hold several ticket types at once, the total is worked out for you, and the request is rejected if there aren't enough tickets left.
- Issue tickets for a booking, each with its own ticket code.
- Record a payment against a booking. It only goes through if the amount covers the booking total. (Payments are simulated for now, there's no real payment gateway yet.)
- See how many tickets an event has sold and how much money it has made.

## Built with

Python 3.12, FastAPI, SQLAlchemy, MySQL (PyMySQL), Pydantic, python-jose for JWT, Argon2 for password hashing, pytest, and Docker.

## How it's organised

```
main.py                     # creates the app, CORS, and registers the routers
app/
├── routers/                # HTTP endpoints (auth, events, ticket types, booking, tickets, payments)
├── services/               # business rules
├── repositories/           # data access
│   ├── *_repository.py     #   abstract interfaces
│   ├── SQL*Repository.py   #   MySQL versions used by the real app
│   └── in_memory_*.py      #   in-memory versions used by tests
├── models/                 # Pydantic models and enums (request/response shapes)
├── database_models/        # SQLAlchemy table definitions
├── core/security.py        # JWT and password hashing
├── dependencies.py         # wires repositories into services
├── database.py             # database connection
└── test/                   # unit tests
```

The idea is that each layer only talks to the one below it. A router calls a service, and the service calls a repository interface. Because the services only depend on the interface, I can test them with the in-memory repositories and swap in the SQL ones when the app runs. `dependencies.py` is where that wiring happens.

## Diagrams

The design diagrams are in the repo:

- [ERD](Event_Ticketing_System_ERD.png)
- [Class diagram](Event%20Ticketing%20System%20Class%20Diagram-3.pdf)
- Use case diagram (`Event Ticketting System-UseCase.drawio`)

## Running it

You need Python 3.12+ and a MySQL database.

```bash
git clone https://github.com/BIGDUKE004/Event-Ticketing-System.git
cd Event-Ticketing-System
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create the database first (the table definitions are created automatically when the app starts):

```sql
CREATE DATABASE Event_Ticketting_System;
```

Then make a `.env` file in the project root:

```env
username=your_mysql_user
password=your_mysql_password
database_name=Event_Ticketting_System
```

and a second one at `app/.env` for the token secret:

```env
JWT_SECRET=some-long-random-string
```

Start the server:

```bash
uvicorn main:app --reload
```

The API is at `http://127.0.0.1:8000` and FastAPI's interactive docs are at `http://127.0.0.1:8000/docs`, where you can try every endpoint.

When it's deployed, I set `DATABASE_URL` (and `JWT_SECRET`) as environment variables instead. If `DATABASE_URL` is set, it's used instead of the local settings above.

### Docker

```bash
docker build -t event-ticketing-api .
docker run -p 8000:8000 \
  -e DATABASE_URL="mysql+pymysql://user:password@host/dbname" \
  -e JWT_SECRET="some-long-random-string" \
  event-ticketing-api
```

### Tests

```bash
pytest
```

The tests cover authentication, events, ticket types, tickets, bookings and payments. They use the in-memory repositories, so you don't need MySQL running.

## Endpoints

Open `/docs` for the full list with request bodies. Here's the overview:

**Auth** (`/auth`)

| Method | Path | |
|---|---|---|
| POST | `/auth/register` | create an account |
| POST | `/auth/login` | log in, returns a token |
| POST | `/auth/logout` | log out |
| PUT | `/auth/update` | update a user |
| DELETE | `/auth/delete/{user_id}` | delete a user |
| GET | `/auth/GetInformation` | the logged-in user's details |

**Events** (`/events`)

| Method | Path | |
|---|---|---|
| POST | `/events/` | create an event |
| GET | `/events/` | list all events |
| GET | `/events/search?keyword=` | search events |
| GET | `/events/{event_id}` | one event with its ticket types |
| GET | `/events/{event_id}/tickets_sold` | tickets sold |
| GET | `/events/{event_id}/amount_made` | money made |
| PATCH | `/events/{event_id}` | update an event |
| DELETE | `/events/{event_id}` | delete an event |

**Ticket types** (`/ticket-types`)

| Method | Path | |
|---|---|---|
| POST | `/ticket-types/` | add a ticket type to an event |
| GET | `/ticket-types/{ticket_type_id}` | one ticket type |
| GET | `/ticket-types/event/{event_id}` | all ticket types for an event |
| PUT | `/ticket-types/{ticket_type_id}` | update |
| DELETE | `/ticket-types/{ticket_type_id}` | delete |

**Booking** (`/booking`)

| Method | Path | |
|---|---|---|
| POST | `/booking/register_booking` | make a booking (needs login) |
| POST | `/booking/update_booking` | update a booking |
| GET | `/booking/get_booking_information/{booking_id}` | one booking |
| GET | `/booking/user/{user_id}` | a user's bookings |
| DELETE | `/booking/delete_booking` | delete a booking |

**Tickets** (`/tickets`) cover creating a ticket, getting one, getting all tickets for a booking, and deleting one.

**Payments** (`/payments`)

| Method | Path | |
|---|---|---|
| POST | `/payments/` | pay for a booking |
| GET | `/payments/` | all payments |
| GET | `/payments/{booking_id}` | the payment for a booking |

For protected endpoints, send the token as `Authorization: Bearer <token>`.

## Things to know

- CORS only allows my deployed frontend (`https://eventpadi-steel.vercel.app`). If you run your own frontend, add its address in `main.py`.
- The database connection always asks for SSL, which suits my hosted MySQL. If your local MySQL doesn't use SSL and the connection fails, remove `connect_args` in `app/database.py`.
- Payments are simulated. A payment is marked successful when the amount is at least the booking total.

## Still to do

- Require login on more endpoints and check that users can only touch their own data
- Connect a real payment provider such as Paystack
- Fix the booking and payment status so a booking becomes successful once it's paid
- Generate QR codes for tickets
- Add pagination to the event list

## Author

Elijah Miracle, [@BIGDUKE004](https://github.com/BIGDUKE004)
