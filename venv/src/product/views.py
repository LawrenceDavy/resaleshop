from django.shortcuts import render
from .models import Product, ProductImages


# get all products
def productlist(request):
    productlist = Product.objects.all()
    context = {'product_list' : productlist}
    template = 'Product/product_list.html'
    return render(request, template, context)



# get all the data of one product
def productdetail(request, product_slug):
    productdetail = Product.objects.get(slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)
    context = {'product_detail' : productdetail, 'prodcut_images': productimages}
    template = 'Product/product_detail.html'
    return render(request, template, context)
