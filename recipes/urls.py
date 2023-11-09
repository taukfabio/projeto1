from django.urls import path
from django.views.static import serve
import os

from . import views


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
FLUTTER_WEB_APP = os.path.join(BASE_DIR, 'recipes', 'templates', 'quiz')
print(FLUTTER_WEB_APP)

def flutter_redirect(request, resource):
    return serve(request, resource, FLUTTER_WEB_APP)


urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
    path('contato/', views.contato),
    path('sobre/', views.sobre),
    

]
