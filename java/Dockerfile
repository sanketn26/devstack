FROM theiaide/theia-java

LABEL maintainer="Sanket Naik <sanketn@gmail.com>"
LABEL version="1.0"
LABEL description="A Java 8, theia based ide with Git, kubefwd and maven settings"

ARG GIT_USER_NAME
ARG GIT_USER_EMAIL

RUN git config --global user.name ${GIT_USER_NAME} \
    && git config --global user.email ${GIT_USER_EMAIL}

RUN mkdir -p /home/theia/.ssh \
    && mkdir -p /home/theia/.m2 \
    && mkdir -p /home/theia/.kube \
    && mkdir -p /home/theia/kfwd

COPY settings.xml /home/theia/.m2/
COPY id_rsa /home/theia/.ssh/
COPY id_rsa.pub /home/theia/.ssh/
COPY known_hosts /home/theia/.ssh/
COPY config /home/theia/.kube
COPY kubefwd /home/theia/kfwd
ENV PATH=$PATH:/home/theia/kfwd