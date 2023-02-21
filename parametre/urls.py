from django.urls import path
from parametre import views

app_name="parametre"
urlpatterns = [

	path('', views.index, name='index'),

]