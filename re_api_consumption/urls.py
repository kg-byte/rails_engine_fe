from django.urls import path
from . import views
urlpatterns = [
				path('merchants', views.merchants, name = 'merchants'),
				path('merchants/<int:merchant_id>', views.merchant, name = 'merchant')
				]