from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path
from authentication.api.views import LoginApiView


urlpatterns = [

    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', LoginApiView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]














# from django.urls import path
# from  authentication.api.views import users


# urlpatterns = [
#     path('users/', users, name='users'),
    
# ]
