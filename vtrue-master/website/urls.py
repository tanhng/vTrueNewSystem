from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
app_name='website'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('intro/',views.intro,name='intro'),
    path('news/',views.news,name='news'),
    path('company/',views.company,name='company'),
    path('feedback/',views.feedback,name='feedback'),
    path('register/',views.register,name='register'),
    path('sign-in/',views.sign_in,name='sign-in'),
    path('count/',views.count,name='count-history'),
    path('check/',views.check.as_view(),name='check'),
    path(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),
]

