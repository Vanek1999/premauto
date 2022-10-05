from django.shortcuts import render, redirect
from .models import Oil, Spares, Autochemistry, Users
from .forms import UserForm, Cart


#-----Забираем ip-----
def get_ip(request):
	oil = Oil.objects.all()
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[-1].strip()
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip

#-----Забираем компоненты-----
def get_components(request):
	ip = get_ip(request)
	try:
		user_cart = Users.objects.get(ip=ip)
		cart = user_cart.cart.split(",")
	except:
		user_cart = ''
		cart = ""
	oil = Oil.objects.all()
	autochemistry = Autochemistry.objects.all()
	spares = Spares.objects.all()
	amount_cart = 0

	for i in cart:
		if i == "":
			pass
		else:
			amount_cart += 1

	return user_cart, cart, oil, autochemistry, spares, amount_cart

#-----Забираем количество товаров-----
def get_info():
	amount_oil = 0
	amount_autochemistry = 0
	amount_spares = 0

	oil = Oil.objects.all()
	for i in oil:
		amount_oil += 1

	autochemistry = Autochemistry.objects.all()
	for i in autochemistry:
		amount_autochemistry += 1

	spares = Spares.objects.all()
	for i in spares:
		amount_spares += 1
	amount_all = amount_oil + amount_autochemistry + amount_spares

	return amount_spares, amount_oil, amount_autochemistry, amount_all, oil, autochemistry, spares

#-----Забираем остальные данные-----
def get_data(request):
	data_all = []
	for i in get_components(request)[1]:
		if i == "":
			pass
		else:
			for components in get_components(request)[3], get_components(request)[4], get_components(request)[2]:
				for component in components:
					if "{}".format(component) == "{}".format(i):
						data_all.append(component)
	price = 0
	for i in data_all:
		price += int(i.product_price)
	all_price = price + 20

	return data_all, price, all_price

#-----Показываем страницы с нужным контентом-----
def index(request):
	return render(request, 'main/index.html', {'oil': get_components(request)[2], "data_all": get_data(request)[0], "price": get_data(request)[1], "all_price": get_data(request)[2], "amount_cart": get_components(request)[5]})

def about_us(request):
	return render(request, 'main/about-us.html', {"data_all": get_data(request)[0], "price": get_data(request)[1], "all_price": get_data(request)[2], "amount_cart": get_components(request)[5]})

def shop(request):
	ip = get_ip(request)

	#-----Обрабатываем форму-----
	if request.method == "POST":
		ip = get_ip(request)
		MyLoginForm = Cart(request.POST or None)
		if MyLoginForm.is_valid():
			product_title = MyLoginForm.cleaned_data.get('product_title')
			product_description = MyLoginForm.cleaned_data.get('product_description')
			product_price = MyLoginForm.cleaned_data.get('product_price')
			old_product = Users.objects.get(ip=ip).cart
			if old_product == None:
				old_product = ""
			if product_title in old_product:
				pass
			else:
				Users.objects.filter(ip=ip).update(cart=old_product + "," + product_title)
		return redirect("/shop")

	return render(request, 'main/shop.html', {'oil': get_info()[4], 'autochemistry': get_info()[5], 'spares': get_info()[6], 'amount_oil': get_info()[1], 'amount_autochemistry': get_info()[2], 'amount_spares': get_info()[0], 'amount_all': get_info()[3], "data_all": get_data(request)[0], "price": get_data(request)[1], "all_price": get_data(request)[2], "amount_cart": get_components(request)[5]})

def my_account(request):
	ip = get_ip(request)

	try:
		ip_user = Users.objects.get(ip = ip)
		return render(request, "main/my-account.html", {"error": "Вы уже авторизовались!", "data_all": get_data(request)[0], "price": get_data(request)[1], "all_price": get_data(request)[2], "amount_cart": get_components(request)[5]})
	except:
		#-----Обрабатываем форму-----
		if request.method == "POST":
			MyLoginForm = UserForm(request.POST)
			if MyLoginForm.is_valid():
				password = MyLoginForm.cleaned_data['password']
				number = MyLoginForm.cleaned_data['number']
				name = MyLoginForm.cleaned_data['name']
				Users.objects.create(password=password, name=name, number=number, ip=ip)
				return render(request, "main/my-account.html", {"error": "Вы успешно авторизовались!", "data_all": get_data(request)[0], "price": get_data(request)[1], "all_price": get_data(request)[2], "amount_cart": get_components(request)[5]})
			else:
				MyLoginForm = UserForm()
				return render(request, "main/my-account.html", {"error": "Форма заполнена неверно! Проверьте пароль/номер", "data_all": get_data(request)[0], "price": get_data(request)[1], "all_price": get_data(request)[2], "amount_cart": get_components(request)[5]})
		return render(request, "main/my-account.html", {"data_all": get_data(request)[0], "price": get_data(request)[1], "all_price": get_data(request)[2], "amount_cart": get_components(request)[5]})

def cart(request):
	#-----Обрабатываем форму-----
	if request.method == "POST":
		ip = get_ip(request)
		MyLoginForm = Cart(request.POST)
		if MyLoginForm.is_valid():
			product_title = MyLoginForm.cleaned_data.get('product_title')
			product_description = MyLoginForm.cleaned_data.get('product_description')
			product_price = MyLoginForm.cleaned_data.get('product_price')
			old_product = Users.objects.get(ip=ip)
			data_new = ''
			old_product = old_product.cart.split(",")
			for i in old_product:
				if i == product_title:
					pass
				else:
					data_new = data_new + i + ","
			Users.objects.filter(ip=ip).update(cart = data_new)

	return render(request, 'main/cart.html', {"data_all": get_data(request)[0], "price": get_data(request)[1], "all_price": get_data(request)[2], "amount_cart": get_components(request)[5]})

#----- -----
def oil(request):
	return render(request, 'main/shop.html', {'oil': Oil.objects.all(), 'amount_oil': get_info()[1], 'amount_autochemistry': get_info()[2], 'amount_spares': get_info()[0], 'amount_all': get_info()[3], "data_all": get_data(request)[0], "price": get_data(request)[1], "all_price": get_data(request)[2], "amount_cart": get_components(request)[5]})

#----- -----
def autochemistry(request):
	return render(request, 'main/shop.html', {'autochemistry': Autochemistry.objects.all(), 'amount_oil': get_info()[1], 'amount_autochemistry': get_info()[2], 'amount_spares': get_info()[0], 'amount_all': get_info()[3], "data_all": get_data(request)[0], "price": get_data(request)[1], "all_price": get_data(request)[2], "amount_cart": get_components(request)[5]})

#----- -----
def spares(request):
	return render(request, 'main/shop.html', {'spares': Spares.objects.all(), 'amount_oil': get_info()[1], 'amount_autochemistry': get_info()[2], 'amount_spares': get_info()[0], 'amount_all': get_info()[3], "data_all": get_data(request)[0], "price": get_data(request)[1], "all_price": get_data(request)[2], "amount_cart": get_components(request)[5]})
