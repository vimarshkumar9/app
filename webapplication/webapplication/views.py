from django.shortcuts import render,redirect
from django.urls import reverse
from visualizer.forms import ShareMarketSymbolForm
from visualizer.forms import ShareMarketSymbolForm
from visualizer.models import Company, StockPrice
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def home(request):
    if request.method == 'POST':
        form = ShareMarketSymbolForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            symbol = form.cleaned_data['symbol']
            start_date = form.cleaned_data['year']
            end_date = form.cleaned_data['end']
            start_str = start_date.strftime('%Y-%m-%d')
            end_str = end_date.strftime('%Y-%m-%d')
            kwargs={'symbol': symbol, 'start': start_str, 'end': end_str}
            url = reverse('data', kwargs=kwargs)
            return redirect(url)
    else:
        form = ShareMarketSymbolForm()
    return render(request, 'home.html', {'form': form})


def data(request, symbol, start, end):
    company = Company.objects.get(ticker=symbol)
    prices = StockPrice.objects.filter(ticker=symbol, date__gte=start, date__lte=end).order_by('date')
    # Create DataFrame from StockPrice objects
    prices_df = pd.DataFrame(list(prices.values('date', 'open_price', 'high_price', 'low_price', 'close_price', 'volume')))
    prices_json = prices_df.to_json(orient='records')
    return render(request, 'data.html', {'company': company, 'prices': prices, 'prices_df': prices_df,'prices_json':prices_json})

def about(request):
    return render(request,"about.html")


def stock_prices_api(request, symbol, start_date, end_date):
    prices = StockPrice.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date).order_by('date')
    data = {
        'symbol': symbol,
        'start_date': start_date,
        'end_date': end_date,
        'prices': list(prices.values()),
    }
    return JsonResponse(data)

    









