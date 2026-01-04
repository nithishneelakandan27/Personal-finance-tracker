from django.shortcuts import render,redirect
from .models import Income, Expense
from django.db.models import Sum

def dashboard(request):
    total_income = Income.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense

    return render(request, 'dashboard.html', {
        'income': total_income,
        'expense': total_expense,
        'balance': balance
    })


def add_income(request):
    if request.method == 'POST':
        Income.objects.create(
            title=request.POST['title'],
            amount=request.POST['amount']
        )
        return redirect('dashboard')
    return render(request, 'add_income.html')


def add_expense(request):
    if request.method == 'POST':
        Expense.objects.create(
            title=request.POST['title'],
            amount=request.POST['amount'],
            category=request.POST['category']
        )
        return redirect('dashboard')
    return render(request, 'add_expense.html')
