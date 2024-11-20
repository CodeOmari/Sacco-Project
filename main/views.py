from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from main.app_forms import CustomerForm, DepositForm
from main.models import Customer, Deposits


# Create your views here.
def test(request):
      # Save customer
      # customer_one = Customer(first_name='John', last_name='Doe', email='johndoe@gmail.com',
      #                         dob='1996-09-17', gender='Male', weight=74)
      # customer_one.save()
      # customer_two = Customer(first_name='Sandra', last_name='Molly', email='sandra536@gmail.com',
      #                         dob='2000-03-12', gender='Female', weight=64)
      # customer_two.save()

      # fetch customer
      customer_count = Customer.objects.count() # number of customers in database
      customer_one = Customer.objects.get(id=1) # SELECT * FROM customers WHERE id=1
      print(customer_one)
      customer_two = Customer.objects.get(id=2)  # SELECT * FROM customers WHERE id=1
      print(customer_two)
      customer_three = Customer.objects.get(id=3)  # SELECT * FROM customers WHERE id=1
      print(customer_three)
      customer_four = Customer.objects.get(id=4)  # SELECT * FROM customers WHERE id=1
      print(customer_four)

      # Add Deposit
      deposit_one = Deposits(amount=1350, status=True, customer=customer_one)
      deposit_one.save()
      deposit_two = Deposits(amount=17850, status=True, customer=customer_two)
      deposit_two.save()
      deposit_three = Deposits(amount=8750, status=True, customer=customer_three)
      deposit_three.save()
      deposit_four = Deposits(amount=13850, status=True, customer=customer_four)
      deposit_four.save()

      # Fetch deposits
      deposit_count = Deposits.objects.count()
      return HttpResponse(f"Ok Done!, you have {customer_count} customers and {deposit_count} deposits")


def customers(request):
      data = Customer.objects.all().order_by('-id').values()  # SELECT * FROM customers
      paginator = Paginator(data, 15)
      page = request.GET.get('page', 1)
      try:
            paginated_data = paginator.page(page)
      except  EmptyPage | PageNotAnInteger:
            paginated_data = paginator.page(1)
      return render(request, "customers.html", {"data": paginated_data})


def delete_customer(request, customer_id):
      customer = Customer.objects.get(id=customer_id) # SELECT * FROM customers WHERE id=1
      customer.delete()
      messages.info(request, f"Customer {customer.first_name} was deleted!!")
      return redirect('customers')


def customer_details(request, customer_id):
      customer = Customer.objects.get(id=customer_id)
      deposits = Deposits.objects.filter(customer_id=customer_id)
      total = Deposits.objects.filter(customer=customer).filter(status=True).aggregate(Sum('amount'))['amount__sum']
      return render(request, 'details.html', {"deposits": deposits,
                                              "customer": customer, "total": total})


def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Customer {form.cleaned_data['first_name']} was added!")
            return redirect('customers')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {"form": form})

def update_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, f"Customer {form.cleaned_data['first_name']} was updated!")
            return redirect('customers')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_update_form.html', {"form": form})

def search_customer(request):
    data = Customer.objects.all().order_by('id').values()  # SELECT * FROM customers
    search_term = request.GET.get('search')
    data = Customer.objects.filter( Q(first_name__icontains=search_term) | Q(last_name__icontains=search_term) |
                                    Q(email__icontains=search_term))
    paginator = Paginator(data, 15)
    page = request.GET.get('page', 1)
    try:
        paginated_data = paginator.page(page)
    except  EmptyPage | PageNotAnInteger:
        paginated_data = paginator.page(1)
    return render(request, "customers.html", {"data": paginated_data})

def deposit(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == "POST":
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            depo = Deposits(amount=amount, status=True, customer=customer)
            depo.save()
            messages.success(request, 'Your deposit has been successfully saved')
            return redirect('customers')
    else:
        form = DepositForm()
    return render(request, 'deposit_form.html', {"form": form, "customer": customer})

