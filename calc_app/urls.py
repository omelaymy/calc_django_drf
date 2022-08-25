from django.urls import path
from rest_framework import routers
from .views import BankList, BankViewSet, BankApiList

# path('calc/', include('calc.urls')),
router = routers.SimpleRouter()
router.register(r'api', BankViewSet)

urlpatterns = [
    path('offer', BankList.as_view(), name='bank_list'),
    path('offer_json/', BankApiList.as_view(), name='offer_json'),


]

urlpatterns += router.urls

