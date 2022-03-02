from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm


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