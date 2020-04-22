FROM theiaide/theia-java

LABEL maintainer="Sanket Naik <sanketn@gmail.com>"
LABEL version="1.0"
LABEL description="Allows for configuring a maven settings file with the theiaide/theia-java image"

ARG GIT_USER_NAME
ARG GIT_USER_EMAIL

RUN git config --global user.name ${GIT_USER_NAME}
RUN git config --global user.email ${GIT_USER_EMAIL}
RUN mkdir -p $HOME/.ssh
RUN mkdir -p $HOME/.m2
RUN mkdir -p $HOME/.kube
RUN mkdir -p /home/theia/kfwd

COPY settings.xml $HOME/.m2/
COPY id_rsa $HOME/.ssh/
COPY id_rsa.pub $HOME/.ssh/
COPY config $HOME/.kube
COPY kubefwd /home/theia/kfwd
ENV PATH=$PATH:/home/theia/kfwd
