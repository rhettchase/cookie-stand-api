# LAB - Class 34

## Project: Putting it All Together

### Project Description

This django built web app utilizes Restful API as well as a user facing site. The app includes full CRUD functionality that allows Creating, Reading, Updating and Deleting cookie stands, on both front-end for users and in admin panel. The site also features API routes. Users are required to be authenticated (via Basic authentication or JWT) to access the API. The app utilizes a Postgres database and is run in Docker container. The app includes JWT authentication to the API and a Gunicorn server. Database is hosted at ElephantSQL. Whitenoise is used to handle static files.

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
- copy `.env.sample` file to create a similar `.env` file and configure for a database of your choice
- Note: the example database information below gives instructions for which settings to apply when creating a db in ElephantSQL

```env
SECRET_KEY=secretcodehere
DEBUG=True

ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
ALLOW_ALL_ORIGINS=True

DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME= # user & default database from ElephantSQL
DATABASE_USER= # user & default database from ElephantSQL
DATABASE_PASSWORD= # password from ElephantSQL
DATABASE_HOST= # server from ElephantSQL
DATABASE_PORT=5432
```

#### How to initialize/run your application (where applicable)

- Clone repo
- Create and activate virtual environment
- Create and configure database (e.g., ElephantSQL)
- Create and activate virtual environment
- Install dependencies `pip install -r requirements.txt`
- Create copy of `.env.sample` to a `.env` file
  - update variables with relevant values for your database
  - run command `python -c "import secrets; print(secrets.token_urlsafe())"` in command line to create secret key, then add this to the `.env` file
- See the page in browser by running `python manage.py runserver`
- Open the page via the local server address specified in the terminal
- Sign up and login to create cookie stands

#### Tests

- N/A
