from django import forms
from django.forms.widgets import SelectDateWidget
import datetime

SYMBOL_CHOICES = [
    ('AAPL', 'Apple Inc.'),
    ('ADBE', 'Adobe Inc.'),
    ('AMZN', 'Amazon.com Inc.'),
    ('BAC', 'Bank of America Corp.'),
    ('DIS', 'Walt Disney Co.'),
    ('GOOG', 'Alphabet Inc. Class C'),
    ('HD', 'Home Depot Inc.'),
    ('JNJ', 'Johnson & Johnson'),
    ('JPM', 'JPMorgan Chase & Co.'),
    ('KO', 'Coca-Cola Co.'),
    ('MA', 'Mastercard Inc.'),
    ('MSFT', 'Microsoft Corp.'),
    ('NVDA', 'Nvidia Corp.'),
    ('PG', 'Procter & Gamble Co.'),
    ('TSLA', 'Tesla Inc.'),
    ('UNH', 'UnitedHealth Group Inc.'),
    ('V', 'Visa Inc.'),
    ('WMT', 'Walmart Inc.')
]

class ShareMarketSymbolForm(forms.Form):
    symbol = forms.ChoiceField(choices=SYMBOL_CHOICES, label='Select Share Market Symbol')
    year = forms.DateField(label='Select Year', widget=SelectDateWidget(years=range(2015, 2025)))
    end = forms.DateField(label='Select Year', widget=SelectDateWidget(years=range(2015, 2025)))
