# Teacher Companion
Application that helps students practice its english speaking and confidence,
This tools is using AI to elaborate the proper answer, when the user ask something
besides it gives the user an appropriate level according its selection.

## Requirements
- Docker
- PostgreSQL
- Python 3.xx
- FastAPI last version


## Installation steps
- first we need to build the container typing the following command:
    `$ docker-compose up -d --build`
- After the image was built, you can verify if the database is running typing 
  following command `$ docker-compose exec db psql --username=daniel --dbname=hello_fastapi_dev`