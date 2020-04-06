FROM theiaide/theia-python

LABEL maintainer="Sanket Naik <sanketn@gmail.com>"
LABEL version="1.0"
LABEL description="A Python theia based ide with git, kubefwd and pip settings"

ARG GIT_USER_NAME
ARG GIT_USER_EMAIL

RUN git config --global user.name ${GIT_USER_NAME} \
    && git config --global user.email ${GIT_USER_EMAIL}

RUN mkdir -p /home/theia/.ssh \
    && mkdir -p /home/theia/.pip \
    && mkdir -p /home/theia/.kube \
    && mkdir -p /home/theia/kfwd \
    && mkdir -p /home/configs \
    && mkdir -p /home/libraries

COPY pip.conf /home/theia/.pip/
COPY id_rsa /home/theia/.ssh/
COPY id_rsa.pub /home/theia/.ssh/
COPY known_hosts /home/theia/.ssh/
COPY config /home/theia/.kube
COPY kubefwd /home/theia/kfwd
ENV PATH=$PATH:/home/theia/kfwd
ENV PYTHONPATH="/home/project"

RUN apt update \
    && apt -y install python2.7-dev python-pip libxml2-dev libxslt1-dev libffi-dev libpq-dev libyaml-dev swig build-essential libssl-dev software-properties-common \
    && apt -y install python-pip
