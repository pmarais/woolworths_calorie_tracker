from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from centraal.models import *
from .serializers import *

## Rest Framework
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

## Token Authenticatio, get auttoken submitting your username & password
## curl -i -X POST -H "Content-Type:application/json " http://localhost:8000/api/api-token-auth/ -d '{"username":"email-address","password":"*****"}'

class MeView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.user.auth_token),  # None
        }
        return Response(content)

# ViewSets define the view behavior.
class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all().order_by('-pk')
    serializer_class = FoodSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     print(self.request.user)
    #     # return Rating.objects.all()
    #     return self.request.user.user_urls.all()

# ViewSets define the view behavior.
class PortionViewSet(viewsets.ModelViewSet):
    queryset = Portion.objects.all().order_by('-pk')
    serializer_class = PortionSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # print(self.request.user)
        # return Rating.objects.all()
        return self.request.user.user_portions.all().order_by('-pk')
