from categories.models import CategoryInfo

def add_dynamic_content(request):
     cat = CategoryInfo.objects.all().order_by('categoryName')
     return {'cate':cat}
     
   