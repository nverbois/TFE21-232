FROM python:3.9.1-slim as production

ENV PYTHONUNBUFFERED=1
WORKDIR /app/ 

# RUN apt-get update && apt-get install --yes libgdal-dev
# RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
# RUN export C_INCLUDE_PATH=/usr/include/gdal

COPY requirements/prod.txt ./requirements/prod.txt
RUN pip install -r ./requirements/prod.txt

COPY manage.py ./manage.py
COPY setup.cfg ./setup.cfg
COPY EPL21232 ./EPL21232 

EXPOSE 8080 

FROM production as development

COPY requirements/dev.txt ./requirements/dev.txt
RUN pip install -r ./requirements/dev.txt

COPY . .