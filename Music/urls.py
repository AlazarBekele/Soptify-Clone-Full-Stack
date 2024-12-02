from django.urls import path
from .views import index, login_Page, sign_up, post_page


urlpatterns = [
    path ('', index, name="index"),
    path ('login/', login_Page, name="login"),
    path ('signup/', sign_up, name="sign_up"),
    path ('post/', post_page, name='post_page')
]
