# FastAPI Application with Postgresql and Hanko Authentication

This FastAPI application is a sample implementation with integrated database migrations using Alembic, authentication via Hanko, and managed dependencies with Poetry. Below is a brief README to help you understand and manage this application.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Akachi-Anabanti/fastapi-hanko
cd backend
```

### 2. Install Poetry

Make sure you have Poetry installed. If not, you can install it following the instructions here: [Poetry Installation](https://python-poetry.org/docs/#installation).

### 3. Install Dependencies

Use Poetry to install the project's dependencies:

```bash
poetry install
```

### 4. Database Setup

This application uses Alembic for database migrations. To set up the database, you need to create the database and apply migrations:

```bash
# Create the database (you may need to configure your database connection in app/config.py)
poetry run alembic upgrade head
```

### 5. Configure Hanko Authentication

The application uses Hanko for authentication. Configure your Hanko API credentials in `app/config.py`:

```python
HANKO_API_URL=https://a8ff***m89f8s***904d7.io
```
visit [Hanko Cloud](https://www.cloud.hanko.io) to obtain your api url

### 6. Run the Application

You can start the FastAPI application using Poetry:

```bash
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The application will be accessible at http://localhost:8000.

## Usage

### API Endpoints

1. **Retrieve Items** - GET `/item/`

   Retrieve a list of items. The `limit` and `skip` parameters can be used for pagination. Users with superuser privileges can access all items, while others can only access their own items.

2. **Create Item** - POST `/item/`

   Create a new item. This endpoint requires authentication. The item will be associated with the authenticated user.

3. **Update Item** - PUT `/item/{id}`

   Update an item by providing its `id`. Only the owner of the item can update it. If the item is not found or the user doesn't have sufficient permissions, an error will be raised.

4. **Get Item by ID** - GET `/item/{id}`

   Retrieve an item by its `id`. Users can only access items they own. If the item is not found or the user doesn't have sufficient permissions, an error will be raised.

5. **Delete Item** - DELETE `/item/{id}`

   Delete an item by providing its `id`. Only the owner of the item can delete it. If the item is not found or the user doesn't have sufficient permissions, an error will be raised.

### Authentication

This application uses Hanko for authentication. Make sure to configure Hanko API credentials in `app/config.py` as mentioned earlier.

## Database Migrations

The application uses Alembic for managing database migrations. You can create and apply migrations as needed with Poetry:

```bash
# Create a new migration
poetry run alembic revision --autogenerate -m "Your migration message"

# Apply pending migrations
poetry run alembic upgrade head
```
if you added new models and schemas run

```bash
poetry run alembic revision --autogenerate -m "revision message"
```
to generate a new revision and then apply the migration as above

## Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
