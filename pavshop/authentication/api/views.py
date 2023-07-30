from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    
)
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from authentication.api.serializers import UserProfileTokenSerializer

class LoginApiView(TokenObtainPairView):

    @swagger_auto_schema(responses={200: UserProfileTokenSerializer()})
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


























# from authentication.models import User
# from django.http import JsonResponse
# from authentication.api.serializers import UserSerializer


# # rest framework -> function-based
# from rest_framework.decorators import api_view



# # GET
# def users(request):
#     user_list = User.objects.all()
#     serializer = UserSerializer(user_list, many = True)
#     return JsonResponse(data=serializer.data, safe=False)



# # GET ve POST @api_views ile
# @api_view(http_method_names=['GET', 'POST'])
# def users(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data=serializer.data, safe=False, status = 201)
#         return JsonResponse(data=serializer.errors, safe=False, status = 400)
#     user_list = User.objects.all()
#     serializer = UserSerializer(user_list, context = {'request' : request}, many = True)
#     return JsonResponse(data=serializer.data, safe=False)

