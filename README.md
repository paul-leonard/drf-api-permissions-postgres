# drf-api-permissions-postgres
A website and database to store a libary's collection of books was created using Django web and REST framework and containerized using Docker.  Permissions are established so that only book owners can modify the contents of the postgresql database.

## Lab Submission Pull Requests
[Lab32: Permissions and Postgresql](https://github.com/paul-leonard/drf-api-permissions-postgres/pull/1)

## Release Info
**Author**: Paul Leonard
**Version**: 1.0.0

## Overview
A website and database to store a libary's collection of books was created using Django web and REST framework and containerized using Docker.  Permissions are established so that only book owners can modify the contents of the postgresql database.

## Architecture
Website, consisting of webpages and a postgresql database, created using the Django web framework with full Create, Read, Update, and Delete (CRUD) capabilities which are accessible through the Django REST Frameworks API. The website is containerized using Docker.  Restricted permissions are established to prevent inadvertent modification and deletion of book instances stored in the database.

## Change Log
**0.9.0** 12-22-2020 - Initial beta release
**1.0.0** 1-2-2021 - Initial release


## Credits and Collaborations
- [git reset](https://www.git-tower.com/learn/git/faq/undo-last-commit/)


## Feature Checklist
*Features - Django REST Framework*
- [x] Make your site a DRF powered API as you did in previous lab.
- [x] Adjust project’s permissions so that only authenticated user’s have access to API.
- [x] Add a custom permission so that only author of blog post can update or delete it.
- [x] Add ability to switch user’s directly from browsable API.
*Features - Docker*
- [x] NOTE Refer to demo for built out Dockerfile and docker-compose.yml examples.
- [x] create Dockerfile based off python:3.8-slim
- [x] CHANGED FROM 3.8 TO 3.9 DUE TO BUILD PROBLEM FOR psycopg2 [community issue](https://github.com/psycopg/psycopg2/issues/1200)
- [x] create docker-compose.yml to run Django app as a web service.
- [x] enter docker-compose up --build to start your site.
- [x] add postgres 11 as a service
- [x] Note: It is not required to include a volume so that data can persist when container is shut down.
- [x] Go to browsable api and confirm site properly restricts users based on their permissions.