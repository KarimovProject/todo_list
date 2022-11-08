from django.contrib import admin
from django.urls import path
from api.views import GetUser,Get_all
urlpatterns = [
    path('admin/', admin.site.urls),
    path('getUser/', GetUser.as_view()),
    path('get_All/', Get_all.as_view()),

]

