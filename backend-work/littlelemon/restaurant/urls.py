#define URL route for index() view
from django.urls import path
from .views import index, MenuItemsView, SingleMenuItemView

urlpatterns = [
    path('',index, name='index'),
    path('menu',MenuItemsView.as_view(), name='menu-items' ),
    path('menu/<int:pk>',SingleMenuItemView.as_view(), name= 'single-menu-items'),

]

