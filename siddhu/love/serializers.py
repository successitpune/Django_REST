from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.contact_no = validated_data.get('contact_no', instance.contact_no)
        instance.alternate_no = validated_data.get('alternate_no', instance.alternate_no)
        instance.address = validated_data.get('address', instance.address)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.model_no = validated_data.get('model_no', instance.model_no)
        instance.physical_condition = validated_data.get('physical_condition', instance.physical_condition)
        instance.estimated_price = validated_data.get('estimated_price', instance.estimated_price)
        instance.imei_1 = validated_data.get('imei_1', instance.imei_1)
        instance.imei_2 = validated_data.get('imei_2', instance.imei_2)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def validate(self, data):
        required_fields = ['customer_name', 'contact_no', 'address', 'model_no', 'estimated_price']
        for field in required_fields:
            if field not in data:
                raise serializers.ValidationError(f"{field} is required.")
        return data
