FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN echo python -V
RUN mkdir /code
RUN mkdir /code/db
WORKDIR /code
#ADD ./requirements.txt /code/
RUN pip install -i https://pypi.douban.com/simple django
RUN pip3 install PyMySQL
RUN pip3 install mysqlclient
#RUN pip3 install -r requirements.txt
ADD . /code/