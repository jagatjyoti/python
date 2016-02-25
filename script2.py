import subprocess
import threading
import time
from logging import getLogger

LOG = getLogger('rsync')

class rsync(subprocess.Popen):
    """
    Run rsync as a subprocess sending output to a logger.
    This class subclasses subprocess.Popen
    """

    def log_thread(self,pipe,logger):
        """
        Start a thread logging output from pipe
        """

        # thread function to log subprocess output
        def log_output(out, logger):
            for line in iter(out.readline, b''):
                logger(line.rstrip('\n'))

        # start thread
        t = threading.Thread(target=log_output,
                             args=(pipe, logger))
        t.daemon = True # thread dies with the program
        t.start()

    def __init__(self,src,dest):
        # construct the command line
        # cmd = ['/usr/bin/rsync', '-rlptvHz',
        #        #'--dry-run',
        #        '--size-only',
        #        '--delete',
        #        # '--bwlimit=256',
        #        "/home/techmadmin/Desktop/swp-CSP-Base-6.3.0.0-08-Linux.iso", "/home/techmadmin/"]
        cmd = ['/usr/bin/rsync', '-avz', 'ssh', '--progress', '/home/techmadmin/Desktop/swp-CSP-Base-6.3.0.0-08-Linux.iso', 
          'root@192.168.1.102:/home/techmadmin/']

        # spawn the rsync process
        super(rsync,self).__init__(
            cmd, shell=False,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            bufsize=1, close_fds='posix')

        LOG.debug("Started rsync subprocess, pid %s" % self.pid)
        LOG.debug("Command:  '%s'" % "','".join(cmd))

        # start stdout and stderr logging threads
        self.log_thread(self.stdout,LOG.info)
        self.log_thread(self.stderr,LOG.warn)