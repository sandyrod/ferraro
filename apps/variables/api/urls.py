from django.urls import path
from apps.variables.api.api import VariableAPIView
from apps.variables.api.api import VariableDetailAPIView

urlpatterns = [
    path('variable/', VariableAPIView.as_view(), name = 'variable'),
    path('variable/<int:pk>/', VariableDetailAPIView.as_view(), name = 'variable_api')
]