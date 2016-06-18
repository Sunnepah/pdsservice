import json
# from django.core import serializers
# from django.http import HttpResponse
from pdsservice import settings

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from sparqlwrapper.SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF, TURTLE

SPARQL_ENDPOINT = settings.SPARQL_ENDPOINT
SPARQL_AUTH_ENDPOINT = settings.SPARQL_AUTH_ENDPOINT


@api_view(['GET'])
def index(request):
    return Response({'message': 'ok'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_email(request, user_id):
    try:
        email = query_graph(get_email_graph_uri(user_id))
        value = email[0]["email"]["value"].split(":")[1]

        telephone = query_graph_telephone(get_telephone_graph_uri(user_id))
        phone = telephone[0]["phone"]["value"].split(":")[1]

        address = query_graph_address(get_address_graph_uri(user_id))
        full_address = address[0]["street"]["value"] + "," + address[0]["locality"]["value"] + "," + \
                       address[0]["postal_code"]["value"] + "," + address[0]["country_name"]["value"]

        return Response({"email": value, "telephone":phone, "address":full_address}, status=status.HTTP_200_OK)

    except Exception as e:
        print e.message
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

        query = "SELECT ?email WHERE { GRAPH <" + graph + "> { ?s <http://www.w3.org/2006/vcard/ns#hasEmail> ?o . ?o <http://www.w3.org/2006/vcard/ns#hasValue> ?email} }"
        print query
        sparql.setQuery(query)

        # JSON example
        # print '\n\n*** JSON Example'
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        res = json.dumps(results, separators=(',', ':'))
        print res
        return results['results']['bindings']
    except Exception as e:
        print e.message
        return list()

def query_graph_telephone(graph):
    try:
        sparql = SPARQLWrapper(SPARQL_AUTH_ENDPOINT)
        sparql.setCredentials(settings.VIRTUOSO_USER, settings.VIRTUOSO_PASSW)

        query = "SELECT ?phone WHERE { GRAPH <" + graph + "> { ?s <http://www.w3.org/2006/vcard/ns#hasTelephone> ?o . ?o <http://www.w3.org/2006/vcard/ns#hasValue> ?phone} }"
        print query
        sparql.setQuery(query)

        # JSON example
        # print '\n\n*** JSON Example'
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        res = json.dumps(results, separators=(',', ':'))
        print res
        return results['results']['bindings']
    except Exception as e:
        print e.message
        return list()

def query_graph_address(graph):
    try:
        sparql = SPARQLWrapper(SPARQL_AUTH_ENDPOINT)
        sparql.setCredentials(settings.VIRTUOSO_USER, settings.VIRTUOSO_PASSW)

        query = "SELECT ?street,?locality,  ?postal_code, ?country_name" \
                " WHERE { GRAPH <" + graph + "> { ?s <http://www.w3.org/2006/vcard/ns#hasAddress> ?add . " \
                "?add <http://www.w3.org/2006/vcard/ns#street-address> ?street . " \
                "?add <http://www.w3.org/2006/vcard/ns#locality> ?locality . " \
                "?add <http://www.w3.org/2006/vcard/ns#postal-code> ?postal_code . " \
                "?add <http://www.w3.org/2006/vcard/ns#country-name> ?country_name } }"

        print query
        sparql.setQuery(query)

        # JSON example
        # print '\n\n*** JSON Example'
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        res = json.dumps(results, separators=(',', ':'))
        print res
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
