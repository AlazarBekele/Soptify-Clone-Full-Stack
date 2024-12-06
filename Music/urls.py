from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
  index,
  login_Page,
  sign_up,
  post_page,
  payment
)


urlpatterns = [
    path ('', index, name="index"),
    path ('login/', login_Page, name="login"),
    path ('signup/', sign_up, name="sign_up"),
    path ('post/', post_page, name='post_page'),
    path ('payment/', payment, name="pay")
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)