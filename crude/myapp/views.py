from django.shortcuts import render,redirect
from .models import ProductDetails
import os

def product(request):
    return render(request,'product.html')

def add_details(request):
    if request.method=='POST':
        pdtname=request.POST['pdtname']
        des=request.POST['des']
        quantity=request.POST['quantity']
        price=request.POST['price']
        photo=request.FILES.get('photo')
        product=ProductDetails(productname=pdtname,description=des,quantity=quantity,price=price,image=photo)
        product.save()
        return redirect('show')
    
def show(request):
    pdt=ProductDetails.objects.all()
    return render(request,'show.html',{'product': pdt})    

def edit(request,pk):
    pdt=ProductDetails.objects.get(id=pk)
    return render(request,'edit.html',{'product':pdt})

def edit_details(request,p):
    if request.method=='POST':
        product=ProductDetails.objects.get(id=p)
        product.productname=request.POST.get('pdtname')
        product.description=request.POST.get('des')
        product.quantity=request.POST.get('quantity')
        product.price=request.POST.get('price')
        newimage=request.FILES.get('photo')
        if newimage:
            if product.image:
                os.remove(product.image.path)
                product.image=newimage 
        product.save()
        return redirect('show')
    return render(request,'edit.html')

def delete(request,pk):
    product=ProductDetails.objects.get(id=pk)
    product.delete()
    return redirect('show')










