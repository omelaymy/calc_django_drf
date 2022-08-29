from django.urls import path
from rest_framework import routers
from .views import BankList, BankViewSet, BankApiList

# path('calc/', include('calc.urls')),
router = routers.SimpleRouter()
router.register(r'api', BankViewSet)

urlpatterns = [
    path('', BankList.as_view(), name='bank_list'),
    path('offer/', BankApiList.as_view(), name='offer'),


]

urlpatterns += router.urls

