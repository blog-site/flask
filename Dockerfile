FROM python:3.11

RUN pip install flask
RUN pip install flask-jwt-extended
RUN pip install mysql-connector-python

ENTRYPOINT ["python","/app/app.py"]
EXPOSE 5000
