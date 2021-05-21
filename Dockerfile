FROM python:latest
WORKDIR /app
COPY holamundo.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 3000
#CMD [ "python3", "holamundo.py"]