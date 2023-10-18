from django.urls import path
from django.views.static import serve
import os

from recipes.views import home, contato, sobre, quiz_flutter


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
FLUTTER_WEB_APP = os.path.join(BASE_DIR, 'recipes', 'templates', 'quiz')
print(FLUTTER_WEB_APP)

def flutter_redirect(request, resource):
    return serve(request, resource, FLUTTER_WEB_APP)


urlpatterns = [
    path('recipes', home),
    path('contato/', contato),
    path('sobre/', sobre),
    path('quiz/', quiz_flutter),
    # path('', flutter_redirect),
    path('', lambda r: flutter_redirect(r, 'index.html')),
    path('<path:resource>', flutter_redirect),
    path('web/', lambda r: flutter_redirect(r, 'index.html')),
    

]
