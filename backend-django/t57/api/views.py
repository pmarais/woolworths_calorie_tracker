from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from centraal.models import *
from .serializers import *

## Rest Framework
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

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

class MeTodayView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'status': get_todays_tally(request.user),  # None
        }
        return Response(content)

class HypotheticalView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'status': get_todays_tally(request.user),  # None
        }
        return Response(content)

    ## Testing Django REST backend {"food_id": 9, "weight": 270}
    def post(self, request):
        if request.method == 'POST':
            # serializer.save()
            food_id = request.data['food_id']
            weight = request.data['weight']
            try:
                food = Food.objects.get(pk=food_id)
                ratio = weight/100
                cals = food.f_kcal*ratio
                fat = food.f_total_fat*ratio
                carbs = food.f_carb*ratio
                fibre = food.f_fibre*ratio
                sugar = food.f_sugar*ratio
            # nonce = request.data['nonce']
                responsedata = {'food': str(food), 'weight': weight, 'cals': cals, 'fat': fat, 'carbs': carbs, 'sugar':sugar, 'fibre': fibre}
                return Response(responsedata, status=status.HTTP_200_OK)
            except:
                pass
        else:
            return Response(False, status=status.HTTP_405_METHOD_NOT_ALLOWED)

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
