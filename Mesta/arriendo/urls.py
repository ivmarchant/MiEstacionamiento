from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/', views.perfil, name='perfil'),
    path('registrar/', views.registrar, name='registrar'),
    path('login/', LoginView.as_view(template_name='log/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='log/logout.html'), name='logout'),
    path('estacionamiento/', views.estacionamiento, name='estacionamiento'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)