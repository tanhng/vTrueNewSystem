from django.urls import path,include
from . import views
app_name='user'
urlpatterns = [
    path('register/',views.signup,name='signup'),
    path('login/',views.signin.as_view(),name='signin'),
]