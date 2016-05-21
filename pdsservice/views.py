# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import paramiko
import settings


@api_view(['POST'])
def accept_command(request):
    try:
        if request.method == 'POST':
            # TODO Proper logging for what comes in
            print "+++++++Request++++++++++"
            data = request.data
            print data["cmd"]
            if execute_virtuoso_sql(data["cmd"]):
                return Response({'message': True}, status=status.HTTP_200_OK)
            else:
                 return Response({'message': False}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({
                'message': False
            }, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'response': 'No content'}, status=status.HTTP_404_NOT_FOUND)


def execute_virtuoso_sql(cmd):
    if not cmd.endswith(";"):
        cmd = "%s;" % cmd

    ssh = paramiko.SSHClient()
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # TODO Use RSA for the authentication
        if ssh.connect(settings.VIRTUOSO_HOST, username=settings.SERVER_USER,
                       password=settings.SERVER_PASSWD):
            print "connected"

        if "DB.DBA" in cmd:
            # exec="DB.DBA.USER_CREATE('185804764220139124118', 'secret');"
            cmd = 'isql-vt 1111 dba dba exec="' + cmd + '"'
        else:
            # cmd = "isql-vt 127.0.0.1:1111 dba dba exec='select count(*) from sys_users;'"
            cmd = "isql-vt 1111 dba dba exec='" + cmd + "'"

        print cmd

        stdin, stdout, stderr = ssh.exec_command(cmd)

        print("Reading outputs from the remote command")
        if stdout:
            for l in stdout:
                print("stdout : %s" % l.strip())
            return True

        if stderr:
            for l in stderr:
                print("stderr : %s" % l.strip())
            return False
    except:
        return False
    finally:
        print "closing connection"
        ssh.close()
        print "closed"
