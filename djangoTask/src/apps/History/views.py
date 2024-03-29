from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ClientHistorySerializer, SalesDealerHistorySerializer, SupplierSalesHistorySerializer
from .models import PurchaseHistory, SalesDealerHistory, SupplierSalesHistory
from djangoTask.src.core.tools.permissions import IsCarDealerAdmin, IsSupplierAdmin
from ...core.tools.mixins import SafeDestroyModelMixin


class CarDealerSalesHistoryViewSet(viewsets.ModelViewSet, SafeDestroyModelMixin):
    queryset = SalesDealerHistory.objects.filter(is_active=True)
    serializer_class = SalesDealerHistorySerializer
    permission_classes = (IsCarDealerAdmin,)


class ClientHistoryViewSet(viewsets.ModelViewSet, SafeDestroyModelMixin):
    queryset = PurchaseHistory.objects.filter(is_active=True)
    serializer_class = ClientHistorySerializer
    permission_classes = (IsAuthenticated,)


class SupplierHistoryViewSet(viewsets.ModelViewSet, SafeDestroyModelMixin):
    queryset = SupplierSalesHistory.objects.filter(is_active=True)
    serializer_class = SupplierSalesHistorySerializer
    permission_classes = (IsSupplierAdmin,)

