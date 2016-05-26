import json
# from django.core import serializers
# from django.http import HttpResponse
from pdsservice import settings

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from SPARQLWrapper.Wrapper import SPARQLWrapper, JSON

SPARQL_ENDPOINT = settings.SPARQL_ENDPOINT
SPARQL_AUTH_ENDPOINT = settings.SPARQL_AUTH_ENDPOINT


@api_view(['GET'])
def index(request):
    return Response({'message': 'ok'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_email(self):
    try:
        user_id = str(self.kwargs['user_id'])
        email = query_graph(get_email_graph_uri(user_id))

        return Response({'email': email}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'response': 'No content'}, status=status.HTTP_404_NOT_FOUND)


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
