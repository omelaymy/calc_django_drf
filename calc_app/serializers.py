from rest_framework import serializers

from .models import Bank


# Для ListApi
class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context:
            representation['credit'] = self.context['credit']
            representation['first_payment'] = self.context['first_payment']
            representation['term'] = self.context['term']
            representation['monthly_payment'] = instance.monthly_payment
            return representation
        return representation


# Для ViewSet
class BankSerializerAPI(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = '__all__'
