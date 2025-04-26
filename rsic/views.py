from django.shortcuts import get_object_or_404, render
from sliderImages.models import ImageSlider
from categories.models import CategoryInfo
from products.models import ProductInfo
from enquiry.models import Enquries

# def homePage(request):
#     return render(request,'index.html')

def robots(request):
    return render(request,'robots.txt')

def siteMap(request):
    return render(request,'sitemap.xml')

def homePage(request):
    imgData = ImageSlider.objects.all()
    prod = ProductInfo.objects.all().order_by('?').values_list('photo', flat=True)
    data ={'imgData':imgData,'title':'Home',"prod":prod}
    return render(request,'index.html',data)

def productPage(request):
    cat = CategoryInfo.objects.all().order_by('categoryName')
    prod = ProductInfo.objects.all().order_by('category_id')
    data = {'cat':cat,'prod':prod,'title':'Products'}
    return render(request,'products.html',data)

def franchisee(request):
    return render(request,'franchisee.html',{'title':'Franchisee'})

def aboutUs(request):
    return render(request,'about.html',{'title':'About Us'})

def contactUs(request):
     cat = CategoryInfo.objects.all().order_by('categoryName')
     r=""
     if request.method=="POST":
            try:
             name= request.POST.get("txtName")
             email= request.POST.get("txtEmail")
             phone= request.POST.get("txtMobile")
             sub= request.POST.get("ddlSubject")
             msg=request.POST.get("msg")
             
             if name == "":
                # r= '*Name is required!'
                raise Exception('*Name is required')
             elif email=="":
                 r= '*Email is required!'
             elif phone=="":
                 r= '*Phone no. is required!'
             elif sub=="":
                 r= '*Subject is required!'
             elif msg=="":
                 r= '*Message is required!'
            except Exception as e:
                r=str(e)
            else:
                result= Enquries(name=name,email=email,phone=phone,subject=sub,msg=msg)
                result.save()
                r="Your response has been received. We'll get back to you shortly. Thanks."
            #  else:
            #     #  raise Exception("Name is required")
            #     #  return render(request,'contact.html',{"error":True})
            #     result= Enquries(name=name,email=email,phone=phone,subject=sub,msg=msg)
            #     result.save()
            #     r="Your response has been received. We'll get back to you shortly. Thanks."

     
     
    #  except ValueError as e:
    #         # Handle the error by adding the error message to the context
    #         context['error_message'] = str(e)
      #  except Exception as e:
      #  return render(request,'contact.html',{ "rel": str(e)})
        
     data = {'cate':cat,'title':'Contact Us','rel':r}
     return render(request,'contact.html',data)

# only works with debug False in settings
def error_404_view(request,exception):
    return render(request,'404.html')


def product_list(request, cat_slug):
    cat = CategoryInfo.objects.all().order_by('categoryName')
    category = get_object_or_404(CategoryInfo, slug=cat_slug)
    prod = ProductInfo.objects.filter(category=category)
    print(prod)
    data={'cat':cat,'prod':prod,'title':'Products'}
    return render(request, 'products.html',data)