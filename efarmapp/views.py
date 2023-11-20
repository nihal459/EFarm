from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'general/index.html')


def farmer_registration(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'farmer/farmer_registration.html')
        else:
            user = User.objects.create_user(
                username=uname,
                password=passw,
                is_farmer=True,
            )
            # Add a success message
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('index')
    else:
        return render(request, "farmer/farmer_registration.html")
    

def farmer_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')

        user = User.objects.filter(username=uname).first()
        
        if user is not None and user.check_password(passw) and user.is_farmer:
            login(request, user)
            return redirect('farmer_home')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'farmer/farmer_login.html')

def farmer_home(request):
    return render(request, 'farmer/farmer_home.html')




def farmer_profile(request, pk):
    get_profile = get_object_or_404(User, pk=pk)


    if request.method == "POST":
        new_name = request.POST.get('name')
        new_mob = request.POST.get('mob')
        new_profile_picture = request.FILES.get('profile_picture')
        new_location = request.POST.get('location')
        new_district = request.POST.get('district')
        new_address = request.POST.get('address')
        bank_name = request.POST.get('bank_name')
        bank_account_number = request.POST.get('bank_account_number')
        ifsc_code = request.POST.get('ifsc_code')
        upi_id = request.POST.get('upi_id')

        if new_profile_picture:
            get_profile.profile_picture = new_profile_picture

        get_profile.name = new_name
        get_profile.mobile_number = new_mob
        get_profile.location = new_location
        get_profile.address = new_address
        get_profile.district = new_district
        get_profile.bank_name = bank_name
        get_profile.bank_account_number = bank_account_number
        get_profile.ifsc_code = ifsc_code
        get_profile.upi_id = upi_id

        # Handle checkboxes for fruits and vegetables
        get_profile.fruits = request.POST.get('fruits') == 'on'
        get_profile.vegetables = request.POST.get('vegetables') == 'on'

        get_profile.save()
 
    context = {'get_profile': get_profile}
    return render(request, 'farmer/farmer_profile.html', context)




def view_shops(request):
    shops = User.objects.filter(is_shop=True)
    context = {'shops':shops}
    return render(request, 'farmer/view_shops.html',context)

def viewshopsingle(request,pk):
    shops = get_object_or_404(User, pk=pk)
    shopid = shops.pk
    pricechart = Pricechart.objects.filter(shopid=shopid)
    context = {'shops':shops, 'pricechart':pricechart}
    return render(request, 'farmer/viewshopsingle.html',context)


def product_chart(request, pk):
    get_productchart = Productchart.objects.filter(farmerid=pk)

    if request.method=="POST":
        item_name = request.POST.get('item_name')
        fruits = request.POST.get('fruits') == 'on'
        vegetables = request.POST.get('vegetables') == 'on'


        farmername = request.user.name
        farmerid = request.user.pk
        farmerusername = request.user.username
        phone_number = request.user.mobile_number

    
        Productchart.objects.create(
            farmerid=farmerid,
            farmerusername=farmerusername,
            farmername=farmername,
            phone_number=phone_number,
            fruits=fruits,
            vegetables=vegetables,
            item_name=item_name,
        )

    context={'get_productchart':get_productchart}

    return render(request, 'farmer/product_chart.html', context)



def edit_productchart(request,pk):
    productchart = get_object_or_404(Productchart, pk=pk)

    if request.method=="POST":

        item_name = request.POST.get('item_name')
        fruits = request.POST.get('fruits') == 'on'
        vegetables = request.POST.get('vegetables') == 'on'

        productchart.item_name = item_name
        productchart.fruits =fruits
        productchart.vegetables =vegetables
        productchart.save()

    context={'productchart':productchart}
    return render(request, 'farmer/edit_productchart.html', context)


def delete_productchart(request,pk):
    productchart = get_object_or_404(Productchart, pk=pk)
    productchart.delete()
    return redirect('farmer_home')

def business(request,pk):
    shops = get_object_or_404(User, pk=pk)
    shopid = shops.pk
    shopusername= shops.username
    shopname = shops.name

    if request.method=="POST":
        item_name = request.POST.get('item_name')
        fruits = request.POST.get('fruits') == 'on'
        vegetables = request.POST.get('vegetables') == 'on'

        farmername = request.user.name
        farmerid = request.user.pk
        farmerusername = request.user.username

        Business.objects.create(
            farmerid = farmerid,
            farmerusername = farmerusername,
            farmername = farmername,
            shopid =shopid, 
            shopusername = shopusername,
            shopname = shopname,
            item_name = item_name,
            fruits = fruits,
            vegetables =vegetables

        )

    context={'shops':shops}
    return render(request, 'farmer/business.html', context)



def farmer_business(request, pk):
    business = Business.objects.filter(farmerid=pk)
    context = {'business':business}
    return render(request, 'farmer/farmer_business.html', context)





def update_farmerbusiness(request, pk):
    business = get_object_or_404(Business, pk=pk)

    context = {'business':business}
    return render(request, 'farmer/update_farmerbusiness.html', context)


def farmer_accept_business(request, pk):
    business = get_object_or_404(Business, pk=pk)

    business.farmer_accept = True
    business.save()

    url = reverse('farmer_business', kwargs={'pk': business.farmerid})

    return redirect(url)


def amount_received(request, pk):
    business = get_object_or_404(Business, pk=pk)

    business.amount_received = True
    business.save()

    url = reverse('farmer_business', kwargs={'pk': business.farmerid})

    return redirect(url)


def products_delivered(request, pk):
    business = get_object_or_404(Business, pk=pk)

    business.farmer_delivered = True
    business.save()

    url = reverse('farmer_business', kwargs={'pk': business.farmerid})

    return redirect(url)

def view_doctors(request):
    doctors = Doctor.objects.all()
    context ={'doctors':doctors}

    return render(request, 'farmer/view_doctors.html', context)


def delete_farmerbusiness(request,pk):
    business = get_object_or_404(Business, pk=pk)

    business.delete() 

    url = reverse('farmer_business', kwargs={'pk': business.farmerid})

    return redirect(url)



def SignOut(request):
     logout(request)
     return redirect('farmer_login')

############################################################################################################################################################################
############################################################################################################################################################################
############################################################################################################################################################################
############################################################################################################################################################################
############################################################################################################################################################################
############################################################################################################################################################################

def shop_registration(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'shop/shop_registration.html')
        else:
            user = User.objects.create_user(
                username=uname,
                password=passw,
                is_shop=True,
            )
            # Add a success message
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('index')
    else:
        return render(request, "shop/shop_registration.html")
    

def shop_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')

        user = User.objects.filter(username=uname).first()
        
        if user is not None and user.check_password(passw) and user.is_shop:
            login(request, user)
            return redirect('shop_home')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'shop/shop_login.html')


def shop_home(request):
    return render(request, 'shop/shop_home.html')



def shop_profile(request, pk):
    get_profile = get_object_or_404(User, pk=pk)


    if request.method == "POST":
        new_name = request.POST.get('name')
        new_mob = request.POST.get('mob')
        new_profile_picture = request.FILES.get('profile_picture')
        new_location = request.POST.get('location')
        new_district = request.POST.get('district')
        new_address = request.POST.get('address')

        if new_profile_picture:
            get_profile.profile_picture = new_profile_picture

        get_profile.name = new_name
        get_profile.mobile_number = new_mob
        get_profile.location = new_location
        get_profile.address = new_address
        get_profile.district = new_district

        # Handle checkboxes for fruits and vegetables
        get_profile.fruits = request.POST.get('fruits') == 'on'
        get_profile.vegetables = request.POST.get('vegetables') == 'on'

        get_profile.save()

    context = {'get_profile': get_profile}
    return render(request, 'shop/shop_profile.html', context)


def price_chart(request,pk):
    get_pricechart = Pricechart.objects.filter(shopid=pk)

    if request.method == "POST":

        item_name = request.POST.get('item_name')
        item_price = request.POST.get('price')
        fruits = request.POST.get('fruits') == 'on'
        vegetables = request.POST.get('vegetables') == 'on'
        
        shopname = request.user.name
        shopid = request.user.pk
        shopusername = request.user.username
        phone_number = request.user.mobile_number
        address = request.user.address
        district = request.user.district
        location = request.user.location

        Pricechart.objects.create(
            shopid=shopid,
            shopusername=shopusername,
            shopname=shopname,
            phone_number=phone_number,
            address=address,
            district=district,
            location=location,
            fruits=fruits,
            vegetables=vegetables,
            item_name=item_name,
            item_perkg=item_price
        )

         
    
    context = {'get_pricechart':get_pricechart}

    return render(request, 'shop/price_chart.html', context)




def delete_pricechart(request,pk):
    pricechart = get_object_or_404(Pricechart, pk=pk)
    pricechart.delete()
    return redirect('shop_home')


def edit_pricechart(request,pk):
    pricechart = get_object_or_404(Pricechart, pk=pk)

    if request.method=="POST":

        item_name = request.POST.get('item_name')
        item_price = request.POST.get('price')
        fruits = request.POST.get('fruits') == 'on'
        vegetables = request.POST.get('vegetables') == 'on'

        pricechart.item_name = item_name
        pricechart.item_perkg=item_price
        pricechart.fruits =fruits
        pricechart.vegetables =vegetables
        pricechart.save()

    context={'pricechart':pricechart}
    return render(request, 'shop/edit_pricechart.html', context)



def view_farmers(request):
    farmers = User.objects.filter(is_farmer=True)
    context = {'farmers':farmers}
    return render(request, 'shop/view_farmers.html',context)




def shop_business(request, pk):
    business = Business.objects.filter(shopid=pk)
    context = {'business':business}
    return render(request, 'shop/shop_business.html', context)



def update_shopbusiness(request,pk):
    business = get_object_or_404(Business, pk=pk)

    if request.method=="POST":
        item_quantity = request.POST.get('item_kg')
        amount = request.POST.get('amount')

        business.item_kg =item_quantity
        business.amount =amount
        business.save()

    context={'business':business}
    return render(request, 'shop/update_shopbusiness.html', context)



def shop_accept_business(request, pk):
    business = get_object_or_404(Business, pk=pk)

    business.shop_accept = True
    business.save()

    url = reverse('shop_business', kwargs={'pk': business.shopid})

    return redirect(url)


def amount_paid(request,pk):
    business = get_object_or_404(Business, pk=pk)

    business.amount_paid = True
    business.save()

    url = reverse('shop_business', kwargs={'pk': business.shopid})

    return redirect(url)

def products_received(request,pk):
    business = get_object_or_404(Business, pk=pk)

    business.shop_received = True
    business.save()

    url = reverse('shop_business', kwargs={'pk': business.shopid})

    return redirect(url)


def viewfarmersingle(request,pk):
    farmers = get_object_or_404(User, pk=pk)
    farmerid = farmers.pk
    productchart = Productchart.objects.filter(farmerid=farmerid)
    context = {'farmers':farmers, 'productchart':productchart}
    return render(request, 'shop/viewfarmersingle.html',context)

def shop_business_request(request,pk):
    
    farmers = get_object_or_404(User, pk=pk)
    farmerid = farmers.pk
    farmerusername= farmers.username
    farmername = farmers.name

    if request.method=="POST":
        item_name = request.POST.get('item_name')
        item_quantity = request.POST.get('item_kg')
        amount = request.POST.get('amount')


        shopname = request.user.name
        shopid = request.user.pk
        shopusername = request.user.username

        Business.objects.create(
            farmerid = farmerid,
            farmerusername = farmerusername,
            farmername = farmername,
            shopid =shopid, 
            shopusername = shopusername,
            shopname = shopname,
            item_name = item_name,
            item_kg = item_quantity,
            amount =amount

        )

    context={'farmers':farmers}

    return render(request, 'shop/shop_business_request.html')




def delete_shop_business(request,pk):
    business = get_object_or_404(Business, pk=pk)

    business.delete() 

    url = reverse('shop_business', kwargs={'pk': business.shopid})

    return redirect(url)


def manage_doctors(request):

    doctors = Doctor.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        Doctor.objects.create(
            name = name,
            phone = phone,
            email = email,

        )
    context={'doctors':doctors}
    return render(request, 'shop/manage_doctors.html', context)

def delete_doctor(request,pk):
    doctor = get_object_or_404(Doctor, pk=pk)

    doctor.delete() 

    return redirect('manage_doctors')

def SignOut2(request):
     logout(request)
     return redirect('shop_login')