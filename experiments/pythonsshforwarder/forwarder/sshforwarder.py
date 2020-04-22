import os
import logging
import signal
from multiprocessing import Process, Value
from sshtunneler import Tunneler

wrapped_control_value = Value('i', 0)

def starttunneler(port, control_value):
    tunneler = Tunneler(port, control_value)
    tunneler.run()

def terminateProcess(signalNumber, frame):
    logging.info('(SIGTERM) terminating the process')
    wrapped_control_value.value = 1
    
if __name__ == '__main__':
    # register the signals to be caught
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    signal.signal(signal.SIGTERM, terminateProcess)
    comma_separated_port_string = os.getenv("COMMA_SEPARATED_FORWARDED_PORTS")
    ports = [int(port) for port in comma_separated_port_string.split(",")]

    childs = []
    for port in ports:
        logging.info("Starting forwaring for port: {}".format(port))
        p = Process(target=starttunneler, args=(port,wrapped_control_value))
        p.start()
        childs.append(p)

    # Lets now wait for the childs to finish up
    for p in childs:
        p.join()
    logging.info("I am done.... forwarding for now...")