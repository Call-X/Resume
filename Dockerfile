FROM python:alpine3.16

ENV PORT=5500
ENV KEY=A035C8C19219BA821ECEA86B64E628F8D684696D
ENV ALLOWED_HOSTS=127.0.0.1
ENV DEBUG=False
WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD gunicorn main:app --bind 0.0.0.0:$PORT
