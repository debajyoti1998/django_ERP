from django.shortcuts import render ,HttpResponse , redirect
from products.models import Products
from django.core import serializers
# Create your views here.

def products_home(request):
    
    if request.user.is_authenticated == False :
        return redirect ('login')

    all_products = Products.objects.all()
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
        #price = request.POST['price']
        image = request.POST['image']
        if(name != None  and image != None):
            add_product=Products(name=name,image=image)
            add_product.save()
            return HttpResponse('Data saved successfully')
        else:
            return HttpResponse('missing element')
    else:
        return render(request,'products/add_product.html')
   



      