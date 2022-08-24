from django.urls import path
from rest_framework import routers
from .views import BankList

# path('calculator/', include('calculator.urls')),
router = routers.SimpleRouter()

urlpatterns = [
    path('', BankList.as_view(), name='bank_list'),
]

urlpatterns += router.urls
