from unicodedata import name
from django.urls import path
from apps.orders.api.api import OrderAPIView, OrderDetailAPIView, OrderListsAPIView, OtiHistoryAPIView, OrderByUserAPIView

urlpatterns = [
    path('orden/', OrderAPIView.as_view(), name = 'orden'),
    path('orden/<int:pk>/', OrderDetailAPIView.as_view(), name = 'orden_api'),
    path('ordenproduccion/<int:pk>/', OrderListsAPIView.as_view(), name = 'orden_list'),
    path('oti_history/', OtiHistoryAPIView.as_view(), name = 'create_oti_history'),
    path('oti_history/<int:pk>/', OtiHistoryAPIView.as_view(), name = 'oti_history'),
    path('otibyuser/<int:pk>/', OrderByUserAPIView.as_view(), name= 'oti_user')

]