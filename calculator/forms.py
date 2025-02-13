from django import forms

class LoanCalculatorForm(forms.Form):
    loan_amount = forms.FloatField(
        label='Loan Amount (€)',
        min_value=0.01,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the loan amount',
            'step': '0.01'
        })
    )
    
    annual_interest_rate = forms.FloatField(
        label='Annual Interest Rate (%)',
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Spread + Euribor',
            'step': '0.01'
        })
    )
    
    years = forms.IntegerField(
        label='Number of Years',
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the loan term in years'
        })
    )