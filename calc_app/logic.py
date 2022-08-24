from django.db.models import F


def monthly_payment(summa, term, rate):
    monthly_rate = F(rate)/100/12
    term = term * 12
    return summa * (monthly_rate + (monthly_rate / (((1 + monthly_rate) ** term) - 1)))
