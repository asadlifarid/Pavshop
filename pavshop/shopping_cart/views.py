from django.conf import settings
from django.shortcuts import render, redirect

from shopping_cart.models import *
from .forms import Shipping_addressForm, Billing_addressForm
from base.models import AbstractModel

from django.urls import reverse_lazy

from django.core.exceptions import ValidationError

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout


from authentication import views
from products.models import *
from django.http import JsonResponse
import json
import datetime

from django.views.decorators.csrf import csrf_exempt


from django.contrib.auth import get_user_model, authenticate

User = get_user_model()




# Generic View import'lar
from django.views.generic import CreateView, FormView, View,TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import ContextMixin



# from shopping_cart.models import Order, OrderItem

# Create your views here.
def shopping_cart_page(request):
    
    if request.user.is_authenticated:
        Customer.objects.get_or_create(user=request.user)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_items.all()
        cartItems = order.get_cart_items
        print(cartItems, '111111111111')
    else:
        items = []
        order = {'get_grand_total' : 0, 'get_cart_items' : 0}
        cartItems = order['get_cart_items']
        print(cartItems, '222222222222222')
       
    top_rated = Product.objects.annotate(Count("reviews"))
    rate_list = [i for i in top_rated if float(i.average_rating()) >= 3][:3]

    context = {
        'items' : items, 
        'order' : order,
        'cartItems' : cartItems,
        'top_rated' : top_rated,
        'rate_list' : rate_list
        }

    return render(request, 'shopping-cart.html', context)







@csrf_exempt
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)


    Customer.objects.get_or_create(user=request.user)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0 or action == "delete":
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)












# Create your views here.
@login_required(login_url='login_page')
def checkout_page(request):
    
    form = Shipping_addressForm()
    if request.method == "POST" and 'submit' in request.POST:
        print(form, "form is here")
        form = Shipping_addressForm(data=request.POST)
        print('form sent !!!!!!')
        if form.is_valid():
            print('form is valid')
            ship = form.save(commit=False)
            ship.user = request.user
            print(ship.user)
            ship.save()
            return redirect(reverse_lazy('checkout_page'))
        else:
            form = Shipping_addressForm()

    


    form = Billing_addressForm()
    if request.method == "POST" and 'continue' in request.POST:
        print(form, "form is here")
        form = Billing_addressForm(data=request.POST)
        print('form sent !!!!')
        if form.is_valid():
            print('form is valid')
            bill = form.save(commit=False)
            bill.user = request.user
            print(bill.user)
            bill.save()
            
            return redirect(reverse_lazy('checkout_page'))
        else:
            form = Billing_addressForm()



    if request.user.is_authenticated:
        Customer.objects.get_or_create(user=request.user)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_items.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_grand_total' : 0, 'get_cart_items' : 0}
        cartItems = order['get_cart_items']

    
    top_rated = Product.objects.annotate(Count("reviews"))
    rate_list = [i for i in top_rated if float(i.average_rating()) >= 3][:3]
    
        

    context = {
        'shipform' : form,  # key hisse, .html'de yazilir, value hisse ise views.py'da qeyd olunur
        'billform' : form,
        'items' : items,
        'order' : order,
        'cartItems' : cartItems,
        'top_rated' : top_rated,
        'rate_list' : rate_list
    }



    return render(request, 'checkout.html', context=context)



@csrf_exempt
def processOrder(request):
    print('Data:', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    # print(transaction_id)
    print(data)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        # total = data['form']['total']
        order.transaction_id = transaction_id

        # if total == order.get_grand_total:
        
        if order.get_grand_total:
            order.complete = True
        order.save()
    else:
        print('User is not logged in.. ')
        
    return JsonResponse('Payment complete!', safe=False)






# Generic View
class CheckoutView(TemplateView):

    ship_form_class = Shipping_addressForm
    bill_form_class = Billing_addressForm
    template_name =  'checkout.html'


    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context["shipform"] =Shipping_addressForm
         context["billform"] =Billing_addressForm
         return context


    def post(self, request):
        post_data = request.POST 
        print(post_data,"++++++")
        
     
        ship_form = self.ship_form_class(post_data)
        bill_form = self.bill_form_class(post_data)

        context = self.get_context_data(ship_form=ship_form, bill_form=bill_form)

        print(context, '1111111111111111111111')
        
        if post_data and 'submit' in post_data:
            if ship_form.is_valid():
                print('validddddddddddddddddd')
                self.form_save(ship_form)

        if post_data and 'continue' in post_data:
            if bill_form.is_valid():
                print('commnettttttttt')
                self.form_save(bill_form)

        return self.render_to_response(context)     


    def form_save(self, form):
        obj = form.save(commit=False)
        obj.user=self.request.user
        obj.save()
        messages.success(self.request, "{} saved successfully".format(obj))
        return obj


    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)




