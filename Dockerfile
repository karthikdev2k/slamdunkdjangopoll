#location for source = C:\Kar\DevOps\Slamdunk_hackathon\myweb
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN apt-get update 
RUN apt-get install net-tools
RUN apt-get -y install iputils-ping
RUN apt-get -y install iproute2

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
