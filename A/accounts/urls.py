from django.urls import path
from . import views
from rest_framework import routers
from rest_framework.authtoken import views as auth_token
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from .views import UserViewSet

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('api-token-auth/', auth_token.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]
router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls


#
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MzU2NTk1MSwiaWF0IjoxNjUzNDc5NTUxLCJqdGkiOiJhNTliOWQ0NTMzYjU0YWUyYTBiMmY4YzE2YTE1YjJkNiIsInVzZXJfaWQiOjh9.8Kb10jbqoT6F8TBACYjiU9I4AzstFgwTX_mcvESkn0o",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzNDc5ODUxLCJpYXQiOjE2NTM0Nzk1NTEsImp0aSI6IjU2NDZjOGE0ZmMwYTRmMDdhZTI0ZGM5YWQzYTgwYWRjIiwidXNlcl9pZCI6OH0.Lsl6DZ-ukeqyxrFBiMUXoQogp8Ll3ht2YnnPBgsVUG8"
#