from django.http import HttpResponse
from django.views import generic
from django.shortcuts import redirect, render
from product.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseNotFound
from product.forms import *


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

def is_valid_queryparm(parm):
    return parm != '' and parm is not None

def product_list(request):
    pro = Product.objects.all()
    
    title_query = request.GET.get('title')
    price_from = request.GET.get('price_from')
    price_to = request.GET.get('price_to')
    date = request.GET.get('date')
    variant = request.GET.get('variant')
    
    if is_valid_queryparm(title_query):
        pro = pro.filter(title__icontains=title_query)

    if is_valid_queryparm(price_from):
        pro = pro.filter(price1__lt = price_from)
    if is_valid_queryparm(price_to):
        pro = pro.filter(price1__gte=price_to)
    if is_valid_queryparm(price_from):
        pro = pro.filter(price2__lt = price_from)
    if is_valid_queryparm(price_to):
        pro = pro.filter(price2__gte=price_to)
    if is_valid_queryparm(price_from):
        pro = pro.filter(price3__lt = price_from)
    if is_valid_queryparm(price_to):
        pro = pro.filter(price3__gte=price_to)
    if is_valid_queryparm(price_from):
        pro = pro.filter(price4__lt = price_from)
    if is_valid_queryparm(price_to):
        pro = pro.filter(price4__gte=price_to)

    if is_valid_queryparm(date):
        pro = pro.filter(created_at__date=date)
    if is_valid_queryparm(variant):
        pro = pro.filter(variant1__icontains=variant)
    # filter search end #

    # pagination start #
    all_post = Paginator(pro, per_page=2)
    page_number=request.GET.get('page',1)
    # page_obj=all_post.get_page(page_number)
    page = request.GET.get('page')
    try:
        posts = all_post.page(page)
    except PageNotAnInteger:
        posts = all_post.page(1)
    except EmptyPage:
        posts = all_post.page(all_post.num_pages)
    # pagination end #
    

    
    context = {
        'pro': posts,
        # 'posts': posts,
        'page_number':int(page_number),
        'all_post':all_post,
    }
    return render(request, 'products/list.html', context)


# product create start #
def productcreate(request):
    if request.method == "post":
        title= request.POST['title']
        sku= request.POST['sku']
        description= request.POST['description']
        obj = Product(title=title, sku=sku, description=description)
        obj.save()

    return render(request,'products/create.html')

# product create end #

        # form=ProductCreateForm(request.POST, request.FILES)
        # if form.is_valid():
            
        #     # obj= form.save(commit=True)
        #     # obj.user=request.user
        #     # obj.save()
        #     return redirect('product:product_list')




