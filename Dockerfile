ARG VARIANT="3.10-bullseye"
FROM python:${VARIANT}

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

CMD ["python3", "finder/finder.py" ]