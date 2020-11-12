from django.shortcuts import render
from apps.store.models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


class ProductListView(ListView):
    model = Product
    template_name = 'core/frontpage.html'
    context_object_name = 'products'
    paginate_by = 4
    queryset = Product.objects.filter(is_featured =True)




#def frontpage(request):

 #   products = Product.objects.filter(is_featured = True)

  #  context = {'products':products}
    
   # return render(request,'core/frontpage.html',context)
    
