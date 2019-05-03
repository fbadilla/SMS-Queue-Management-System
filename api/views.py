from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from api.family_datastructure import Family
import json

# initialize a 'Doe' family
family = Family(last_name='Doe')

"""
The MembersView will contain the logic on how to:
 GET, POST, PUT or delete family members
"""
class MembersView(APIView):
    def get(self, request, member_id=None):
        # fill this method and update the return
        result = None
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        # fill this method and update the return
        result = None
        return Response(result, status=status.HTTP_200_OK)

    def put(self, request, member_id=None):
        # fill this method and update the return
        result = None
        return Response(result, status=status.HTTP_200_OK)

    def delete(self, request, member_id=None):
        # fill this method and update the return
        return Response({ "status": "ok" }, status=status.HTTP_200_OK)