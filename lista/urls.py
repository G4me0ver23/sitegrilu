from django.urls import path
from . import views
app_name='lista'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:palavra_id>/infos/',views.infos,name='infos'),
]
