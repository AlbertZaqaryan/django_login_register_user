from django.shortcuts import render, redirect
from .models import Book, Cart
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    book_list = Book.objects.all()
    return render(request, 'index.html', context={
        'book_list':book_list
    })

def cart(request):
    cart_list = Cart.objects.all()
    return render(request, 'cart.html', context={
        'cart_list':cart_list
    })

def add_to_cart(request):
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        user_id = request.POST.get('user_id')
        one_book = Book.objects.get(id=book_id)
        one_user = User.objects.get(id=user_id)
        cart_list = Cart.objects.all()
        for i in cart_list:
            if i.book == one_book and i.user == one_user:
                x = Cart.objects.get(id=i.id)
                x.count += 1
                x.cart_price += i.book.price
                x.save()
                break
        else:
            Cart.objects.create(book=one_book, user=one_user, count=1, cart_price=one_book.price)
        return redirect('index')
    

def delete_from_cart(request):
    if request.method == 'POST':
        cart_object_id = request.POST.get('cart_object_id')
        cart_object = Cart.objects.get(id=cart_object_id)
        if cart_object.count > 1:
            cart_object.count -= 1
            cart_object.cart_price -= cart_object.book.price
            cart_object.save()
        else:
            Cart.objects.filter(id=cart_object_id).delete()
        return redirect('cart')
    

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")


def user_page(request):
    book_list = Book.objects.filter(user=request.user)
    return render(request, 'user_page.html', context={
          'book_list':book_list
    })


def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        user = request.user
        Book.objects.create(name=name, author=author, price=price, image=image, user=user)
        return redirect('user_page')
    return render(request, 'add_book.html', context={
          
    })