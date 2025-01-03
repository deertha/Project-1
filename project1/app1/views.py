from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import ReservationForm
# Create your views here.
def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')
def menu (request) :
    items = {
    'menu': Menu.objects.all
    }
    return render (request, 'menu.html', items)

def about(request):
    return render(request,'about.html')


from .forms import *

from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReservationForm

def reserve_table(request):
    form = ReservationForm()  # Always initialize form here
    
    success_message = None  # Flag for success message

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the reservation to the database
            success_message = "Reservation created successfully!"  # Set success message
        else:
            return render(request, 'reserve.html', {'form': form, 'error': 'Invalid form submission'})

    return render(request, 'reserve.html', {'form': form, 'success_message': success_message})



from django.shortcuts import render, redirect
from .models import Menu, Order, OrderItem

# View for displaying the menu and placing an order
def place_order(request):
    if request.method == 'POST':
        # Get data from the form
        customer_name = request.POST.get('customer_name')
        customer_contact = request.POST.get('customer_contact')
        selected_items = request.POST.getlist('menu_items')  # List of selected menu items
        quantities = request.POST.getlist('quantities')  # List of quantities for each item
        
        # Create a new order
        order = Order.objects.create(customer_name=customer_name, customer_contact=customer_contact)
        
        # Create order items and link them to the order
        for item_id, quantity in zip(selected_items, quantities):
            menu_item = Menu.objects.get(id=item_id)
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=int(quantity))
        
        # Calculate the total price of the order
        order.calculate_total_price()
        
        # Redirect to the success page
        return redirect('order_success')

    # Fetch all menu items for displaying
    menu_items = Menu.objects.all()
    return render(request, 'place_order.html', {'menu_items': menu_items})

# Success page after order is placed
def order_success(request):
    return render(request, 'order_success.html')

