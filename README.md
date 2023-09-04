## Movie API

### Project Structure:

![Screenshot (70)](https://github.com/anuj0809/backend../blob/main/1.png)

### Setting Up the Environment:

Open a terminal/command prompt.

Navigate to the MovieAPIApp directory.

Create a virtual environment named "env" (you can replace "env" with your preferred name):

    python -m venv env

Activate the virtual environment:

    For Windows: env\Scripts\activate
    For Linux/Mac: source env/bin/activate

Installing Dependencies:

    pip install -r requirements.txt

Setting Flask App Environment:

    For Windows: set FLASK_APP=app.py
    For Linux/Mac: export FLASK_APP=app.py

Database Setup:

    Create the database: flask create_db
    Populate the database: flask populate_db

Running the Application:

    Run application: flask run

### Using the API:

To Log In:

        Send a POST request to http://127.0.0.1:5000/login.

        Include your username and password in the request body as JSON.

To Get All Movies:

        Send a GET request to http://127.0.0.1:5000/api/movies.

To Search for Movies Based on Parameters:

        Send a GET request to http://127.0.0.1:5000/api/movies.

        Add your query parameters in the query field.

To Add a Movie:

        Send a POST request to http://127.0.0.1:5000/api/movies.

        Include the movie information in the request body as JSON.

        Add an authentication header in the format: Authorization: Bearer your_access_token.

To Edit a Movie:

        Send a PUT request to http://127.0.0.1:5000/api/movies/<movie_id>.

        Include the updated movie information in the request body as JSON.

        Add an authentication header in the format: Authorization: Bearer your_access_token.

To Delete a Movie:

        Send a DELETE request to http://127.0.0.1:5000/api/movies/<movie_id>.

        Add an authentication header in the format: Authorization: Bearer your_access_token.

Replace <movie_id> with the actual ID of the movie you want to edit or delete. Ensure that you have a valid access token when making authenticated requests.
