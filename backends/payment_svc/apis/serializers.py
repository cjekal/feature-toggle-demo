from rest_framework import serializers
from apis.models import Payment
from apis.services import UserService
from apis.features import FeaturesClient


class PaymentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    amount = serializers.FloatField(required=True)
    user_id = serializers.IntegerField(required=True)
    user_name = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        user_id = validated_data.get('user_id')
        return Payment.objects.create(
            amount = self.get_payment_amount(validated_data.get('amount'), user_id),
            user_id = user_id,
            user_name=self.get_user_name(user_id)
        )

    def update(self, instance, validated_data):
        user_id = validated_data.get('user_id', instance.user_id)
        instance.amount = self.get_payment_amount(validated_data.get('amount', instance.amount), user_id)
        instance.user_id = user_id
        instance.user_name = self.get_user_name(user_id)
    
    def get_user(self, user_id):
        return UserService().get_user_details(user_id)

    def get_user_name(self, user_id):
        return self.get_user(user_id)["user_name"]
    
    def get_user_payment_limit(self, user_id):
        return self.get_user(user_id)["payment_limit"]

    def get_payment_amount(self, amount, user_id):
        # feature toggle in action!
        # also, guard-clause!
        if not FeaturesClient().is_enabled("payment-limit-by-user-profile"):
            return amount

        user_payment_limit = self.get_user_payment_limit(user_id)
        if amount > user_payment_limit:
            return user_payment_limit
        
        return amount