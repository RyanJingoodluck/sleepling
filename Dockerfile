FROM silverlogic/python3.6

MAINTAINER Ryan Jin

WORKDIR /sleeping
COPY . /sleeping
COPY conf/pip.conf /root/.pip/pip.conf


# pip配置文件，主要用来指定pip源
RUN pip install -r requirements.txt;
RUN python manage.py collectstatic;

EXPOSE 8000

CMD uwsgi --ini conf/uwsgi.ini