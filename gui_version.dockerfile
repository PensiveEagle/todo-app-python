FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-directory -r requirements.txt

COPY . .

CMD [ "python", "./gui_main.py" ]