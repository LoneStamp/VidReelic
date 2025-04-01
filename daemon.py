import time
import daemon
import logging
from daemon import pidfile


logging.basicConfig(filename='/tmp/daemon.log', level=logging.INFO)


def run_daemon():
    while True:
        logging.info('Daemon is running...')
        time.sleep(10)  

# Main function to start the daemon
def start_daemon():
    with daemon.DaemonContext(
        stdout=open('/tmp/daemon.out', 'w'),
        stderr=open('/tmp/daemon.err', 'w'),
        pidfile=pidfile.TimeoutPIDLockFile('/tmp/daemon.pid')
    ):
        run_daemon()


if __name__ == "__main__":
    start_daemon()
