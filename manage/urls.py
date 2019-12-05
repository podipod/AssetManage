from django.urls import path
from manage import views


app_name = 'manage'


urlpatterns = [
    path('upload/',views.upload,name="upload"),
    path('display/',views.read_data_create,name="display"),
]