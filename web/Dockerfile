# pull official base image
FROM python:3.11.1-slim-buster

# set work directory
WORKDIR /usr/sample-python-project-web

# set Python environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/sample-python-project-web/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY ./web /usr/sample-python-project-web/web
COPY ./sample /usr/sample-python-project-web/sample
COPY ./utils /usr/sample-python-project-web/utils

# set pythonpath
ENV PYTHONPATH "${PYTHONPATH}:/usr/sample-python-project-web"

# annouce needed ports
EXPOSE 5000

# executes our gunicorn
ENTRYPOINT ["./web/gunicorn.sh"]