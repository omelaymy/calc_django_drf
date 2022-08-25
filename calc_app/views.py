from django.db.models import PositiveIntegerField, ExpressionWrapper, Q
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import viewsets, permissions
from django.views.generic import ListView
from rest_framework.generics import ListAPIView


from .models import Bank
from .logic import monthly_payment
from .serializers import BankSerializer, BankSerializerAPI


# Без drf на html странице с простыми формами
class BankList(ListView):
    model = Bank
    template_name = 'bank_list.html'
    context_object_name = 'banks'

    def get_queryset(self):
        queryset = Bank.objects.all().order_by('rate_min')
        request = self.request.GET
        try:
            credit = int(request['credit'])
            first_payment = int(request['first_payment'])
            term = int(request['term'])
            summa = credit - first_payment
            queryset = Bank.objects.filter(Q(payment_min__lte=summa) & Q(payment_max__gte=summa) &
                                           Q(term_min__lte=term) & Q(term_max__gte=term)).order_by('rate_min')
            queryset = queryset.annotate(
                monthly_payment=ExpressionWrapper(monthly_payment(summa, term, rate='rate_min'),
                                                  output_field=PositiveIntegerField()))
            return queryset
        except MultiValueDictKeyError:
            print('Введены неверные данные')
            return queryset
        except ValueError:
            print('Введены неверные данные')
            return queryset


# CRUD drf
class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializerAPI
    permission_classes = [permissions.IsAdminUser]


# Вывод с drf
class BankApiList(ListAPIView):
    serializer_class = BankSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']
    ordering_fields = '__all__'
    ordering = ['rate_min']
    search_fields = ['name']

    def get_queryset(self):
        queryset = Bank.objects.all().order_by('rate_min')
        request = self.request.query_params
        try:
            credit = int(request['credit'])
            first_payment = int(request['first_payment'])
            term = int(request['term'])
            summa = credit - first_payment
            queryset = Bank.objects.filter(Q(payment_min__lte=summa) & Q(payment_max__gte=summa) &
                                           Q(term_min__lte=term) & Q(term_max__gte=term)).order_by('rate_min')
            queryset = queryset.annotate(
                monthly_payment=ExpressionWrapper(monthly_payment(summa, term, rate='rate_min'),
                                                  output_field=PositiveIntegerField()))
            return queryset
        except MultiValueDictKeyError:
            print('Введены неверные данные')
            return queryset
        except ValueError:
            print('Введены неверные данные')
            return queryset

    def get_serializer_context(self):
        if self.request.query_params:
            return {
                'credit': self.request.query_params['credit'],
                'first_payment': self.request.query_params['first_payment'],
                'term': self.request.query_params['term'],
            }
