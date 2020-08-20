FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y \
    libopenblas-dev \
    gfortran \
    libhdf5-dev \
    libgeos-dev \
    openssl \
    wget\
    git

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --user --upgrade setuptools
RUN pip install django-braces
RUN pip install -r requirements.txt
RUN pip uninstall -y cython
RUN apt-get remove -y gfortran

RUN apt-get autoremove -y
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip uninstall --yes numpy
RUN pip install numpy

ADD . /code/

CMD /code/run_uwsgi.sh

EXPOSE 3031
