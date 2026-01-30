FROM python:3.10-slim

#set working dir inside container
WORKDIR /app

#copy requirements.txt
COPY requirements.txt .

#install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy entire project