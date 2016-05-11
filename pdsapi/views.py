# from django.core import serializers
# from django.http import HttpResponse
from pdsservice import settings

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


import paramiko
from SPARQLWrapper.Wrapper import SPARQLWrapper, JSON

SPARQL_ENDPOINT = settings.SPARQL_ENDPOINT
SPARQL_AUTH_ENDPOINT = settings.SPARQL_AUTH_ENDPOINT


@api_view(['GET'])
def index(request):
    return Response({'message': 'ok'}, status=status.HTTP_200_OK)


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


@api_view(['POST'])
def contact_returns(request):
    try:
        return Response({
            'status': 'ok',
            'message': 'fine'
        }, status=status.HTTP_200_OK)
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


@api_view(['GET'])
def get_user_contact(request):
    try:
        return Response({
            'status': 'ok',
            'message': 'fine'
        }, status=status.HTTP_200_OK)
    except:
        return Response({'response': 'No content'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_user_email(request, user_id):
    email = query_graph(get_email_graph_uri(user_id))
    print "User ID -> " + str(user_id)
    return Response({'email': email}, status=status.HTTP_200_OK)

@api_view(['GET'])
def status_check(request):
    try:
        return Response({
            'status': 'ok',
            'message': 'fine'
        }, status=status.HTTP_200_OK)
    except:
        return Response({'response': 'No content'}, status=status.HTTP_404_NOT_FOUND)


def query_graph(graph):
    try:
        sparql = SPARQLWrapper(SPARQL_AUTH_ENDPOINT)
        sparql.setCredentials(settings.VIRTUOSO_USER, settings.VIRTUOSO_PASSW)

        query = "SELECT * WHERE { GRAPH <" + graph + "> { ?s ?p ?o . } }"

        sparql.setQuery(query)

        # JSON example
        # print '\n\n*** JSON Example'
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        # res = json.dumps(results, separators=(',', ':'))
        return results['results']['bindings']
    except Exception as e:
        print e.message
        return list()


def get_email_graph_uri(user_id):
    print settings.GRAPH_ROOT + '/' + user_id + '/emails'
    return settings.GRAPH_ROOT + '/' + user_id + '/emails'


def get_telephone_graph_uri(user_id):
    print settings.GRAPH_ROOT + '/' + user_id + '/telephones'
    return settings.GRAPH_ROOT + '/' + user_id + '/telephones'


def get_address_graph_uri(user_id):
    print settings.GRAPH_ROOT + '/' + user_id + '/addresses'
    return settings.GRAPH_ROOT + '/' + user_id + '/addresses'


def get_person_graph_uri(user_id):
    print settings.GRAPH_ROOT + '/' + user_id + '/persons'
    return settings.GRAPH_ROOT + '/' + user_id + '/persons'
