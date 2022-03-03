from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from django.shortcuts import get_object_or_404
from .models import Image

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from common.decorators import ajax_required

from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger


@login_required
def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            # form data is valid
            print("00000000000000000000")
            cd = form.cleaned_data
            print(cd)
            new_item = form.save(commit=False)
            print(new_item)
            # assign current user to the item
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')
            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)
        print(form)

    return render(request,'images/image/create.html',{'section': 'images','form': form})





def image_detail(request, id, slug):
    print(id,slug)
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request,'images/image/detail.html',{'section': 'images','image': image})


@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'}) 






