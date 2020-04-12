FROM theiaide/theia-java

LABEL maintainer="Sanket Naik <sanketn@gmail.com>"
LABEL version="1.0"
LABEL description="A Java 8, theia based ide with Git, kubefwd and maven settings"

ARG GIT_USER_NAME
ARG GIT_USER_EMAIL

RUN git config --global user.name ${GIT_USER_NAME} \
    && git config --global user.email ${GIT_USER_EMAIL} \
    mkdir -p $HOME/.ssh \
    && mkdir -p $HOME/.m2 \
    && mkdir -p $HOME/.kube \
    && mkdir -p /home/theia/kubetools

COPY settings.xml $HOME/.m2/ \
     id_rsa $HOME/.ssh/ \
     id_rsa.pub $HOME/.ssh/ \
     config $HOME/.kube/ \
     kubefwd /home/theia/kubetools/ \
     stern /home/theia/kubetools/ \
     kubectl /home/theia/kubetools/ 
     
ENV PATH=$PATH:/home/theia/kubetools