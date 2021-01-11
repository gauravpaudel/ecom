from django.shortcuts import render
from apps.store.models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q
from apps.order.models import Order

def order_confirmation(request):
    return render(request,'core/email_confirmation.html')


class ProductListView(ListView):
    model = Product
    template_name = 'core/frontpage1.html'
    context_object_name = 'products'
    paginate_by = 8
    queryset = Product.objects.filter(is_featured =True)


class SearchListView(ListView):
    model = Product
    template_name = 'core/search.html'
    context_object_name = 'products'
    paginate_by = 8
    def get_queryset(self):
        query = self.request.GET.get('q')
        #to use filter in foreign key use string representation of that model 
        object_list = Product.objects.filter(Q(title__icontains=query) | Q(category__title__icontains = query))
        return object_list
    
    def get_context_data(self,**kwargs):
        query = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        context['q'] = query
        return context