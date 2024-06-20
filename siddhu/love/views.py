from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer
from django.shortcuts import get_object_or_404
import logging

logger = logging.getLogger(__name__)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Customer_api(request, id=None):
    try:
        if request.method == 'GET':
            if id is not None:
                customer = get_object_or_404(Customer, id=id)
                serializer = CustomerSerializer(customer)
                return Response(serializer.data)
            else:
                customers = Customer.objects.all()
                serializer = CustomerSerializer(customers, many=True)
                return Response(serializer.data)

        elif request.method == 'POST':
            serializer = CustomerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT':
            customer = get_object_or_404(Customer, id=id)
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            customer = get_object_or_404(Customer, id=id)
            customer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found.'}, status=status.HTTP_404_NOT_FOUND)
    except serializers.ValidationError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f"Unexpected error in Customer_api: {str(e)}")
        return Response({'error': 'Internal server error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
