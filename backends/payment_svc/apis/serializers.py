from rest_framework import serializers
from apis.models import Payment
from apis.services import UserService


class PaymentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    amount = serializers.FloatField(required=True)
    user_id = serializers.IntegerField(required=True)
    user_name = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        return Payment.objects.create(**validated_data, user_name=self.get_user_name(validated_data.get('user_id')))

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        user_id = validated_data.get('user_id', instance.user_id)
        instance.user_id = user_id
        instance.user_name = self.get_user_name(user_id)

    def get_user_name(self, user_id):
        return UserService.new().get_user_details(user_id)["user_name"]