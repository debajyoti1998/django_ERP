import random

from django.shortcuts import render ,HttpResponse , redirect
from products.models import Products
from django.core import serializers
# Create your views here.

def products_home(request):
    
    if request.user.is_authenticated == False :
        return redirect ('login')

    # all_products = Products.objects.all()
    all_products = Products.objects.filter(deleted=0)
    # data = serializers.serialize('json', all_products )
    # print(data)


    context = {
        "products":all_products,
    }
    return render(request,'products/product_home.html' , context)



def add_product(request):
    if request.user.is_authenticated == False :
        return redirect ('login')

    if request.method == "POST":
        name = request.POST['name']
        purchase_price = request.POST['purchase_price']
        sell_price = request.POST['sell_price']
        image = request.FILES['image']
        if(name != None and purchase_price !=None and sell_price !=None ):
            add_product=Products(name=name,purchase_price=purchase_price,sell_price=sell_price,image=image)
            add_product.save()
            return redirect ('/products')
        else:
            return HttpResponse('missing element')
    else:
        context ={
            "loginStatus": request.user.is_authenticated
        }
        return render(request,'products/add_product.html',context)

def delete_product(request,p_id):
    if request.user.is_authenticated == False :
        return redirect ('login')

    Products.objects.filter(id=p_id).update(deleted=1)
    return redirect ('/products')
    
def update_product(request,p_id):
    if request.user.is_authenticated == False :
        return redirect ('login')
        
        
    if request.method == "POST":
        p_name = request.POST['p_name']
        p_purchase_price=request.POST['p_purchase_price']
        p_sell_price=request.POST['p_sell_price']
        if p_name != None and p_name !='' and  p_purchase_price !=None and p_sell_price !=None:
            Products.objects.filter(id=p_id).update(name=p_name,purchase_price=p_purchase_price,sell_price=p_sell_price)
            return redirect ('/products')
        else :
            context ={
                "loginStatus": request.user.is_authenticated,
                'error' : 'no product name received'
            }
            return render(request,'products/update.html', context)
    else:
        context ={
            "loginStatus": request.user.is_authenticated
        }
        return render(request,'products/update.html',context)
   



      