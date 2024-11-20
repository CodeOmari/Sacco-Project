from django.http import HttpResponse

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