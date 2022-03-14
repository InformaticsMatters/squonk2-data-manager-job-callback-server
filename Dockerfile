ARG from_image=python:3.10.2-alpine3.14
FROM ${from_image}

# Force the binary layer of the stdout and stderr streams
# to be unbuffered
ENV PYTHONUNBUFFERED 1

# Base directory for the application
# Also used for user directory
ENV APP_ROOT /home/app

# Containers should NOT run as root
# (as good practice)
RUN adduser -D -h ${APP_ROOT} -s /bin/sh app
RUN chown -R app.app ${APP_ROOT}

COPY requirements.txt ${APP_ROOT}/
RUN pip install -r ${APP_ROOT}/requirements.txt

COPY app.py ${APP_ROOT}/
COPY LICENSE ${APP_ROOT}/

USER app
ENV HOME ${APP_ROOT}
WORKDIR ${APP_ROOT}

EXPOSE 5000
ARG flask_env=development
ENV FLASK_ENV ${flask_env}
CMD flask run --host=0.0.0.0
