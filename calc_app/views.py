from django.db.models import PositiveIntegerField, ExpressionWrapper, Q
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView
from .models import Bank
from .logic import monthly_payment


# Вывод без дрф на HTML странице с элементарными формами
class BankList(ListView):
    model = Bank
    template_name = 'bank_list.html'
    context_object_name = 'banks'

    def get_queryset(self):
        queryset = Bank.objects.all().order_by('rate_min')
        request = self.request.GET
        try:
            deposit = int(request['credit'])
            first_payment = int(request['first_payment'])
            term = int(request['term'])
            summa = deposit - first_payment
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
