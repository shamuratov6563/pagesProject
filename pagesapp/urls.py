from django.urls import path
from .views import HomePageView, AboutPageView, ServicesPageTemplate

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('services/', ServicesPageTemplate.as_view(), name='services')

]