
from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="home"),
    path('host',views.host,name="host"),
    path('updateFav/<int:id>',views.updateFav,name="updateFav")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
