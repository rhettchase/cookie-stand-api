# LAB - Class 34

## Project: Putting it All Together

### Project Description

This django built web app utilizes Restful API as well as a user facing site. The app includes full CRUD functionality that allows Creating, Reading, Updating and Deleting cookie stands, on both front-end for users and in admin panel. The site also features API routes. Users are required to be authenticated (via Basic authentication or JWT) to access the API. The app utilizes a Postgres database and is run in Docker container. The app includes JWT authentication to the API and a Gunicorn server. Whitenoise is used to handle static files.

### Author: Rhett Chase

### Links and Resources

<!-- - [back-end server url](https://capital-finder-rhett-chase.vercel.app/api) -->
<!-- - [front-end application](http://xyz.com/) (when applicable) -->
- chatGPT
- [ElephantSQL](https://api.elephantsql.com/)

### Setup

- `pip install -r requirements.txt`

#### `.env` requirements (where applicable)

<!-- i.e.
- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db -->
- see `.env.sample` for what is required to be completed
- 

#### How to initialize/run your application (where applicable)

- Clone repo
- Create and activate virtual environment
- Install dependencies (see above)
- See the page in browser by running `python manage.py runserver`
- Open the page via the local server address specified in the terminal

##### Create Superuser

- In separate terminal, create superuser with command `python manage.py createsuperuser`
- Visit the `/admin` path and login with the superuser username and password you created

##### Create, Update, Delete Snacks

- **`Read`**: Visit the home directory (snack list) view the full list of snacks `http://127.0.0.1:8000/`
- **`Create`**: Click on `Create New Snack` button and complete the form, then click `Save`
- **`Update` and `Delete`**: Return to home (snack list), then click on a snack you want to delete or update
- Click update or delete
- Confirm your choice (click save to update or OK to delete, depending on the selection)

#### How to use your library (where applicable)

- N/A

#### Tests

- `python manage.py test`

