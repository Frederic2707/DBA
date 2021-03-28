FROM python:3

ENV DATABASE_HOST=localhost
ENV REDIS_HOST=localhost

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "-u", "main.py" ]