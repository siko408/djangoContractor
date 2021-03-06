from django.conf.urls import url
from django.urls import path
# This syntax imports all of the functions and classes
# inside the views.py in the same folder.
from . import views
urlpatterns = [
    path('', views.Homepage.as_view(), name='homePage'),
    path('charityPage/', views.Charitypage.as_view(), name='charityview'),
    path('infoScreen/', views.InfoPage.as_view(), name='info-view'),
    path('newsScreen/', views.NewsPage.as_view(), name='news-view'),
    path('settings/', views.SettingsPage.as_view(), name='settings-view')
]
