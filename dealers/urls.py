from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dealer/<int:pk>/', views.dealer_detail, name='dealer_detail'),
    path('dealer/<int:pk>/review/', views.post_review, name='post_review'),
    path('api/dealers/', views.api_dealers, name='api_dealers'),
    path('api/dealers/<int:pk>/', views.api_dealer_detail, name='api_dealer_detail'),
    path('api/dealers/<int:pk>/reviews/', views.api_reviews, name='api_reviews'),
    path('api/carmakes/', views.api_car_makes, name='api_car_makes'),
    path('api/analyze-review/', views.analyze_review, name='analyze_review'),
]
