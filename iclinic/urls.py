
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from authentication import views

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='iclinic API documentation')

urlpatterns = [

	path('login/', views.LoginView.as_view()),
	path('profile/', views.ProfileView.as_view()),


	
	# DOCUMENTATION
	path('api/docs/', schema_view),

	path('parametre/', include('parametre.urls')),
    path('admin/', admin.site.urls),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



