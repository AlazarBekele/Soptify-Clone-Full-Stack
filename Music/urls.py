from django.urls import path
from .views import index, login_Page


urlpatterns = [
    path ('', index, name="index"),
    path ('login/', login_Page, name="login_Page")
]
