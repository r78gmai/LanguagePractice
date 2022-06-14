FROM ubuntu:20.04

#MAINTAINER test

RUN apt-get update -y && apt-get install -yq wget build-essential gcc zlib1g-dev

WORKDIR /root/
RUN wget https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz \
        && tar zxf Python-3.9.10.tgz \
        && cd Python-3.9.10 \
        && ./configure \
        && make altinstall
ENV PYTHONIOENCODING "utf-8"

WORKDIR /

#RUN apt-get update
#RUN apt-get install python
#RUN apt-get install vim -y
#RUN /usr/local/bin/python -m pip install --upgrade pip

#RUN python -m pip install cycler

CMD ["/bin/bash"]
