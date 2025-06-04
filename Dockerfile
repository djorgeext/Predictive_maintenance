FROM python:3.10

WORKDIR /PREDICTIVE_MAINTENANCE
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /PREDICTIVE_MAINTENANCE/

CMD bash -c "while true; do sleep 1; done"