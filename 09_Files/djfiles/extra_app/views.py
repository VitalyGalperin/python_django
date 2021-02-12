from _csv import reader
from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from .additional_tasks import *


def index(request):
    return render(request, 'extra/index.html')


def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            content = file.name + ' размер: ' + str(file.size) + ' байт'
            if file.content_type == 'text/plain':
                text_file = upload_file_form.cleaned_data['file'].read()
                if check_stop_words(text_file):
                    content += ' Файл не прошел проверку'
                else:
                    content += 'Все хорошо!'
            return HttpResponse(content=content, status=200)
    else:
        upload_file_form = UploadFileForm()
    context = {
        'form': upload_file_form,
    }
    return render(request, 'extra/upload_file.html', context=context)


def upload_files(request):
    if request.method == 'POST':
        form = MultiFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for f in files:
                instance = File(file=f)
                instance.save()
            return HttpResponse(content='Success', status=200)
    else:
        form = MultiFileForm()
    context = {
        'form': form,
    }
    return render(request, 'extra/upload_file.html', context=context)


def item_list(request):
    items = Item.objects.all()
    context = {'items_list': items}
    return render(request, 'extra/items_list.html', context=context)


def upload_price(request):
    if request.method == 'POST' and request.FILES['file']:
        upload_file_form = UploadPriceForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            price_file = upload_file_form.cleaned_data['file'].read()
            price_str = price_file.decode('utf-8').split('\r\n')
            csv_reader = reader(price_str, delimiter=';', quotechar='"')
            for row in csv_reader:
                if row:
                    Item.objects.filter(code=row[0]).update(price=Decimal(row[1]))
            return HttpResponse(content='Success', status=200)
    else:
        upload_file_form = UploadFileForm()
    context = {
        'form': upload_file_form,
    }
    return render(request, 'extra/upload_price_file.html', context=context)


def model_upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(content='Success', status=200)
    else:
        form = DocumentForm()
    context = {
        'form': form,
    }
    return render(request, 'extra/file_form_upload.html', context=context)



