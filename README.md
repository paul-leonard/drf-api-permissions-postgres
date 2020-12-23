# drf-api-permissions-postgres
A website and database to store a libary's collection of books was created using Django web and REST framework and containerized using Docker.  Permissions are established so that only book owners can modify the contents of the postgresql database.

## Lab Submission Pull Requests
[Lab32: Permissions and Postgresql](https://github.com/paul-leonard/drf-api-permissions-postgres/pull/1)

## Release Info
**Author**: Paul Leonard
**Version**: 0.9.0

## Overview
A website and database to store a libary's collection of books was created using Django web and REST framework and containerized using Docker.  Permissions are established so that only book owners can modify the contents of the postgresql database.

## Architecture
Website, consisting of webpages and a postgresql database, created using the Django web framework with full Create, Read, Update, and Delete (CRUD) capabilities which are accessible through the Django REST Frameworks API. The website is containerized using Docker.  Restricted permissions are established to prevent inadvertent modification and deletion of book instances stored in the database.

## Change Log
**0.9.0** 12-22-2020 - Initial beta release
**1.0.0** 11-TBD-2020 - Initial release


## Credits and Collaborations
- [git reset](https://www.git-tower.com/learn/git/faq/undo-last-commit/)