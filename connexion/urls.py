from django.urls import path
from connexion.views import RegisterView, UserView, LoginView, LogoutView


app_name="connexion"
urlpatterns = [
	path('registers/', RegisterView.as_view()),
    path('users/', UserView.as_view()),

	path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

]
