from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pdsservice import settings
import logging

from sql_users import VirtuosoSqlUsers

log = logging.getLogger(__name__)

sqluser = VirtuosoSqlUsers()


@api_view(['POST'])
def new_sql_user(request):
    try:
        if request.method == 'POST':
            log.info("+++++++Received Request++++++++++")
            data = request.data
            if sqluser.create_new_user(data["username"]):
                return Response({'message': True}, status=status.HTTP_200_OK)
            else:
                return Response({'message': False}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({
                'message': False
            }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except:
        return Response({'response': 'No content'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def grant_graph_permission(request):
    try:
        if request.method == 'POST':
            log.info("+++++++Received" \
                  " Request++++++++++")
            data = request.data
            if sqluser.set_user_permission_on_personal_graph(data["username"], data["graph"]):
                return Response({'message': True}, status=status.HTTP_200_OK)
            else:
                 return Response({'message': False}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({
                'message': False
            }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Exception as e:
        print e.message
        return Response({'response': 'No content'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
