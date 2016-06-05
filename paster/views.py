import uuid
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from . import forms, models


def index(request):
    image_list = models.UploadImage.objects.order_by('-uploaded_ts')
    paginator = Paginator(image_list, 12)

    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)

    # Make images suitable for building 4 by 3 grid
    image_grid = (
        images[0:3],
        images[4:7],
        images[8:11],
    )

    page_navs = paginator.page_range[images.number-1:images.number+4]

    return render(
        request,
        'paster/index.html', {
            'image_grid': image_grid,
            'images': images,
            'page_navs': page_navs,
        }
    )


def file_upload(request):
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save()
            return JsonResponse({'file_url': new_file.image.url})
        else:
            return JsonResponse({'error': form.errors})
    else:
        return render(request, 'paster/upload.html')


def full_picture(request, key):
    pass
