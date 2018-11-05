FROM python:3.6-alpine

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN pip install .

ENTRYPOINT ["python", "-m", "discord_labbutler"]