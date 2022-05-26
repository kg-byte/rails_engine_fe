from django.urls import path
from . import views
urlpatterns = [
				path('merchants', views.merchants, name = 'merchants'),
				path('merchants/<int:merchant_id>', views.merchant, name = 'merchant'),
				path('items/<int:item_id>', views.item, name = 'item')
				]