from django.shortcuts import render
from .forms import LoanCalculatorForm

def format_number(number):
    """Format number with 2 decimal places and comma as decimal separator"""
    return f"{number:.2f}".replace('.', ',')

def calculate_loan_payment(loan_amount, annual_interest_rate, years):
    try:
        monthly_rate = (annual_interest_rate / 12) / 100
        number_of_payments = years * 12  
        if monthly_rate == 0:
            return loan_amount / number_of_payments  
        monthly_payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** (-number_of_payments))
        return round(monthly_payment, 2)
    except Exception as e:
        return None

def loan_calculator_view(request):
    result = None
    form = LoanCalculatorForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        loan_amount = form.cleaned_data['loan_amount']
        annual_interest_rate = form.cleaned_data['annual_interest_rate']
        years = form.cleaned_data['years']
        
        monthly_payment = calculate_loan_payment(loan_amount, annual_interest_rate, years)
        if monthly_payment is not None:
            total_payment = monthly_payment * years * 12
            result = {
                'monthly_payment': format_number(monthly_payment),
                'total_payment': format_number(total_payment),
                'total_interest': format_number(total_payment - loan_amount),
                'loan_amount': format_number(loan_amount),
                'rate': format_number(annual_interest_rate),
                'years': years
            }
    
    return render(request, 'calculator/calculator.html', {
        'form': form,
        'result': result
    })