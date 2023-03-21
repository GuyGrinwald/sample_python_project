# pull official base image
FROM python:3.11.1-slim-buster

# set work directory
WORKDIR /usr/sample-python-project-db

# set Python environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/sample-python-project-db/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY ./db /usr/sample-python-project-db

# set pythonpath
ENV PYTHONPATH "${PYTHONPATH}:/usr/sample-python-project-db"

# executes our gunicorn
CMD ["python", "connector.py"]
# CMD ["ls", "-la"]