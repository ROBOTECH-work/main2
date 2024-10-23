from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Product


def home(request):
    return render(request, 'home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def services(request):
    return render(request, 'services.html')

def properties(request):
    return render(request, 'properties.html')

def contact(request):
    return render(request, 'contact.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('main')  # Redirect to main.html
        else:
            # Handle invalid login
            return render(request, 'signin.html', {'error': 'Invalid username or password.'})
    
    return render(request, 'signin.html')

@login_required(login_url='signin')
def main(request):
    return render(request, 'main.html')

def product_detail(request, id):
    product = Product.objects.get(id=id)  # Fetch the product by ID
    return render(request, 'product_detail.html', {'product': product})  # Render detail template

