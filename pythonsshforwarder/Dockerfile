FROM python:buster

LABEL maintainer="Sanket Naik <sanketn@gmail.com>"
LABEL version="1.0"
LABEL description="Acts as a SSH Port forwarder process for being able to forward ports to the docker based dev stack"

RUN mkdir -p /opt/forwarder/
ADD forwarder /opt/forwarder/

ENV SSH_SERVER="localhost"
ENV SSH_SERVER_USER="admin"
ENV SSH_SERVER_PASSWORD="password"
ENV COMMA_SEPARATED_FORWARDED_PORTS="6379,5432,5672,15672"
ENV PYTHONPATH=/opt/forwarder/
RUN pip install --no-cache-dir -r /opt/forwarder/requirements.txt
WORKDIR /opt/forwarder

CMD [ "python3", "./sshforwarder.py" ]