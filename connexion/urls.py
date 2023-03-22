from django.urls import path
from connexion.views import RegisterAPIView, UserAPIView, UsersAPIView, LoginAPIView, LogoutAPIView


app_name="connexion"
urlpatterns = [
	path('registers', RegisterAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('users', UsersAPIView.as_view()),
    path('', LoginAPIView.as_view()),
	path('login', LoginAPIView.as_view()),
	path('logout', LogoutAPIView.as_view()),
]
