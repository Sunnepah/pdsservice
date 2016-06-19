# -*- coding: utf-8 -*-
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#
# Author: Sunnepah

import paramiko
import logging
from pdsservice import settings

log = logging.getLogger(__name__)


class RemoteSql():

    def __init__(self, hostname):
        if type(hostname) == str:
            self.host = settings.VIRTUOSO_HOST
            self.user = settings.SERVER_USER
            self.password = settings.SERVER_PASSWD

        else:
            raise Exception("Incorrect hostname or credentials.")

    def execute_virtuoso_sql(self, cmd):
        print "Entering Execute Virtuoso Sql"
        if not cmd.endswith(";"):
            cmd = "%s;" % cmd

        ssh = paramiko.SSHClient()
        try:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # TODO Use RSA for the authentication
            print self.host
            if ssh.connect(self.host, self.user, self.password):
                print "Connected"

            if "DB.DBA" in cmd:
                # exec="DB.DBA.USER_CREATE('username', 'password');"
                cmd = 'isql-vt 1111 dba dba exec="' + cmd + '"'
            else:
                # cmd = "isql-vt 127.0.0.1:1111 dba dba exec='select count(*) from sys_users;'"
                cmd = "isql-vt 1111 dba dba exec='" + cmd + "'"

            stdin, stdout, stderr = ssh.exec_command(cmd)

            log.info("Reading outputs from the remote command")
            if stdout:
                for l in stdout:
                    log.debug("stdout : %s" % l.strip())
                return True

            if stderr:
                for l in stderr:
                    print "stderr : %s" % l.strip()
                    log.debug("stderr : %s" % l.strip())
                return False
        except Exception as e:
            print e.args
            print "Exception"
            return False
        finally:
            print "Closing connection..."
            ssh.close()
            print "Connection closed"
