from django.shortcuts import render, redirect  # 5-8
from django.contrib.auth.decorators import login_required  # 5-8
from django.contrib import messages  # 5-8
from .forms import ImageCreateForm  # 5-8


# Create your views here.

@login_required
def image_create(request):  # 5-8

    if request.method == 'POST':
        #form is set
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            new_item = form.save(commit=False)

            # assign current user to the item
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')

            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)

    return render(request,
                  template_name='images/image/create.html',
                  context={
                      'section': 'images',
                      'form': form
                  })
