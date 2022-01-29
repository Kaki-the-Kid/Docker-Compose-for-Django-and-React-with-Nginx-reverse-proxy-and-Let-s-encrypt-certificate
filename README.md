# Test to make backend enviroment for React app
## Inspiration
* SaaSitive - Docker-Compose for Django and React with Nginx reverse-proxy and Let's encrypt certificate
https://saasitive.com/tutorial/docker-compose-django-react-nginx-let-s-encrypt/
* Link to the code repository:
https://github.com/saasitive/django-react-boilerplate
* CodingEntrepreneurs - Django + Chart.js // Learn to intergrate Chart.js with Django
https://www.youtube.com/watch?v=B4Vmm3yZPgc
* freeCodeCamp.org - Python Django Web Framework - Full Course for Beginners
https://www.youtube.com/watch?v=F5mRW0jo-U4
* Programming with Mosh - Python Django Tutorial for Beginners
https://www.youtube.com/watch?v=rHux0gMZ3Eg


# Documentation
## Docker - Docker-Compose
[TODO - Rewrite(notcopypaste)]In this Dockerfile the python:3.8.3-alpine is used as base image. Let’s decode this image name and tag. It contains python in version 3.8.3, running in the Linux distribution Alpine which is lightweight. The purpose of using lightweight Linux is to have small image which will result in faster builds. You can of course use different base image. For purpose of this tutorial the python:3.8.3-alpine is sufficient.

We create /app directory in the container and copy /backend/requirements.txt. Then, gunicorn and all needed packages are installed. The backend source code is copied at the end of the container build. It is on purpose. It makes building faster. When you change something in the code (without changing the requirements.txt file), only the last line of the Dockerfile will be executed and the rest will be read from cache (of course if available).

The Dockerfile is not executing any command, we will use wsgi-entrypoint.sh script for this purpose.
## Django
## React
## Nginx reverse proxy
## Let's encrypt certificate
