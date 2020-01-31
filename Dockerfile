FROM python:3.8-alpine

RUN pip install --upgrade pip && \
    pip install pipenv
COPY Pipfile* /
RUN pipenv install --system --ignore-pipfile --deploy
COPY cat.py /

ENV FLASK_APP cat.py
EXPOSE 5000

ENTRYPOINT ["flask"]
CMD ["run", "--host", "0.0.0.0"]
