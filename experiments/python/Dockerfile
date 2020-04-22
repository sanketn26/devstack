FROM theiaide/theia-python

LABEL maintainer="Sanket Naik <sanketn@gmail.com>"
LABEL version="1.0"
LABEL description="Allows for a customer python image with pip conf"

ARG GIT_USER_NAME
ARG GIT_USER_EMAIL

RUN git config --global user.name ${GIT_USER_NAME}
RUN git config --global user.email ${GIT_USER_EMAIL}
RUN mkdir -p $HOME/.ssh
RUN mkdir -p $HOME/.pip
RUN mkdir -p $HOME/.kube
RUN mkdir -p /home/theia/kfwd

COPY pip.conf $HOME/.pip/
COPY id_rsa $HOME/.ssh/
COPY id_rsa.pub $HOME/.ssh/
COPY config /root/.kube

COPY kubefwd /home/theia/kfwd
ENV PATH=$PATH:/home/theia/kfwd

ENV PYTHONPATH="/home/project"

RUN apt update
RUN apt -y install python2.7-dev python-pip libxml2-dev libxslt1-dev libffi-dev libpq-dev libyaml-dev swig build-essential libssl-dev software-properties-common
RUN apt -y install python-pip virtualenv
