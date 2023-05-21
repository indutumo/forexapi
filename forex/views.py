from django.shortcuts import render
import requests
from django.shortcuts import render, redirect
from .forms import ForexRateForm
from .models import ForexRate

api_key = '***********************'

def index(request):
	return render(request,'forex/index.html')


def forex_rate(request):
	
	base_currency = 'USD'
	url = f'https://openexchangerates.org/api/latest.json?app_id={api_key}&base={base_currency}'
	response = requests.get(url)
	print(response.json())
	data = response.json()

	target_currency = ['EUR','GBP','INR','JPY','CNY']
	for i in target_currency:

	    if response.status_code == 200:
	        data = response.json()
	        rate = data['rates'][i]
	        print(f'1 {base_currency} = {rate} {i}')
	        ForexRate.objects.create(base_currency=base_currency,target_currency=i,rate=rate)

	    else:
	        print(f'Request failed with status code {response.status_code}')

	return redirect('index')
	

def forex_rate_list(request):
	qs = ForexRate.objects.order_by('-datetime')[:20]

	context = {
		'forex_rate':qs,
	}
	return render(request,'forex/forex_rate.html', context)


def custom_forex_rate(request):
    #getting information from the form
    if request.method == "POST":
        form = ForexRateForm(request.POST)
        if form.is_valid():
            base_currency = form.cleaned_data['base_currency']
            target_currency = form.cleaned_data['target_currency']

            api_key = '674ae76c2d38498e80a2997a88f46dfa'
            base_currency = 'USD'
            url = f'https://openexchangerates.org/api/latest.json?app_id={api_key}&base={base_currency}'
            response = requests.get(url)
            print(response.json())
            data = response.json()

            if response.status_code == 200:
            	data = response.json()
            	rate = data['rates'][target_currency]
            	print(f'1 {base_currency} = {rate} {target_currency}')
            	ForexRate.objects.create(base_currency=base_currency,target_currency=target_currency,rate=rate)
            else:
            	print(f'Request failed with status code {response.status_code}')
            return redirect('forex_rate_list')
        else:
            print(form.errors)
    return render(request,'forex/forex_form.html')
    