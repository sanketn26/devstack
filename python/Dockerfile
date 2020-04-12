FROM theiaide/theia-python

LABEL maintainer="Sanket Naik <sanketn@gmail.com>"
LABEL version="1.0"
LABEL description="A Python theia based ide with git configured, kubefwd and pip settings"

ARG GIT_USER_NAME
ARG GIT_USER_EMAIL

RUN git config --global user.name ${GIT_USER_NAME} \
    && git config --global user.email ${GIT_USER_EMAIL} \
    mkdir -p $HOME/.ssh \
    && mkdir -p $HOME/.pip \
    && mkdir -p $HOME/.kube \
    && mkdir -p /home/theia/kubetools 

COPY pip.conf $HOME/.pip/ \
     id_rsa $HOME/.ssh/ \
     id_rsa.pub $HOME/.ssh/ \
     config $HOME/.kube/ \
     kubefwd /home/theia/kubetools/ \
     stern /home/theia/kubetools/ \
     kubectl /home/theia/kubetools/

ENV PATH=$PATH:/home/theia/kubetools \
    PYTHONPATH="/home/project" 