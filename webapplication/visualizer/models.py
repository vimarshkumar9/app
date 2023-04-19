from django.db import models

class Company(models.Model):
    ticker = models.CharField(max_length=10, primary_key=True)
    company_name = models.CharField(max_length=255)
    exchange = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'companies'


class StockPrice(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.CharField(max_length=10)
    date = models.DateField()
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
    volume = models.FloatField()
    
    class Meta:
        db_table = 'stock_prices'
        unique_together = (('ticker', 'date'),)



