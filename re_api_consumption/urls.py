from django.urls import path
from . import views

urlpatterns = [
				path('', views.merchants, name = 'merchants'),
				path('merchants/<int:merchant_id>', views.merchant, name = 'merchant'),
				path('items/<int:item_id>', views.item, name = 'item'),
				path('items', views.items, name = 'items'),
				path('search', views.search, name='search')
				]