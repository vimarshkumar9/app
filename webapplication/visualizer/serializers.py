from rest_framework import serializers
from .models import Company, StockPrice

class StockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPrice
        fields = ('date', 'open_price', 'high_price', 'low_price', 'close_price', 'volume')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'ticker', 'exchange')
