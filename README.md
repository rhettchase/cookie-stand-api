# LAB - Class 41

## Project: API Deployment

### Project Description

This django built web app utilizes Restful API as well as a user facing site. The app includes full CRUD functionality that allows Creating, Reading, Updating and Deleting cookie stands, on both front-end for users and in admin panel. The site also features API routes. Users are required to be authenticated (via Basic authentication or JWT) to access the API. The app utilizes a Postgres database and is run in Docker container. The app includes JWT authentication to the API and a Gunicorn server. Database is hosted at ElephantSQL. Whitenoise is used to handle static files.

The API is deployed on Vercel, and requires authentication to access routes.

### Author: Rhett Chase

### Links and Resources

<!-- - [back-end server url](https://capital-finder-rhett-chase.vercel.app/api) -->
<!-- - [front-end application](http://xyz.com/) (when applicable) -->
- chatGPT
- [ElephantSQL](https://api.elephantsql.com/)
- [Vercel](https://vercel.com/docs/frameworks/nextjs)

### Setup

- N/A

#### `.env` requirements (where applicable)

- N/A for deployed site
- See `.env.sample` for example

#### How to initialize/run your application (where applicable)

Front-End

- Visit [front-end deployed site](https://cookie-stand-admin-rhett-chase.vercel.app/)
- Login using username and password created below on the api back-end site
- Add cookie stand
- Note: you can only delete cookie stands that you created with your account

Back-end

- Visit [deployed back-end](https://cookie-stand-api-rhett-chase.vercel.app/) and click on `get started` and `create account` to set up account
- Visit [front-end deployed site](https://cookie-stand-admin-rhett-chase.vercel.app/) to login
- Note: must be authenticated view routes; staff account required for admin actions; restrictions apply to updating and deleting data that you did not create
- View API at route: [https://cookie-stand-api-rhett-chase.vercel.app/api/v1/cookie_stands/](https://cookie-stand-api-rhett-chase.vercel.app/api/v1/cookie_stands/)

#### Tests

- N/A
