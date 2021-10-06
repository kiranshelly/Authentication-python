from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('edit/<id>',edit,name="edit"),
    path('main', main,name="main"),
    path('', login,name="login"),
    path('register', register,name="register"),
    path('logout', logout,name="logout"),
    path('token', token,name="token"),
    path('user_details',user_details,name="user_details"),
    path('user',edit,name="edit"),

]

urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
