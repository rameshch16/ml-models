FROM ubuntu:latest
MAINTAINER Ben Weber

RUN apt-get update \  
  && apt-get install -y python3-pip python3-dev \  
  && cd /usr/local/bin \  
  && ln -s /usr/bin/python3 python
  
RUN pip3 install flask 
RUN pip3 install pandas 
RUN pip3 install gunicorn   
RUN pip3 install scikit-learn 
RUN pip3 install google-cloud-logging 
RUN pip3 install google-cloud-monitoring 
  
COPY serving.json serving.json
COPY app.py app.py

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0", "app:app"]