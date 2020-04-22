from sshtunnel import SSHTunnelForwarder
import traceback
import os
import logging
import time

class Tunneler:
    def __init__(self, port, wrappedControlValue):
        self.remote_server = os.getenv("SSH_SERVER")
        self.remote_user = os.getenv("SSH_SERVER_USER")
        self.remote_password = os.getenv("SSH_SERVER_PASSWORD")
        self.port = port
        self.controlvalue = wrappedControlValue
        logging.basicConfig()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        self.server = SSHTunnelForwarder(
            self.remote_server,
            ssh_username = self.remote_user,
            ssh_password=self.remote_password,
            remote_bind_address=('127.0.0.1', port),
            local_bind_address=('0.0.0.0', port),
            set_keepalive=10.0,
            logger=logger
        )

    def run(self):
        logging.info("starting port forward to {}:{}".format(self.remote_server, self.port))
        try:
            self.server.start()
            while True:
                if self.controlvalue.value == 1:
                    break
                if self.server.is_active:
                    logging.info("Tunnel is up from local to {}:{}".format(self.remote_server, self.port))
                    time.sleep(30)
            self._stop()
        except Exception:
            logging.exception("Error forwarding port to {}:{}".format(self.remote_server, self.port))
        
        
    def _stop(self):
        logging.info("starting port forward to {}:{}".format(self.remote_server, self.port))
        try:
            self.server.start()
        except Exception:
            logging.exception("Error forwarding port to {}:{}".format(self.remote_server, self.port))
