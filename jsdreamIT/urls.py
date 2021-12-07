from django.urls import path, include
from .import views

app_name='jsdreamIT'
urlpatterns = [
    path('', views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('about_us/',views.about,name='about'),
    path('it-service/',views.itservice,name='itservice'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('blog/', views.blog, name='blog'),
    path('search/', views.search_blog, name='search'),
    path('blog/<slug>/', views.blog_details, name='details'),

    
]
