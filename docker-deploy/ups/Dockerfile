FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN pip3 install protobuf
RUN pip3 install --upgrade google-api-python-client
RUN pip3 install google-cloud-translate