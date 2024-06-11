from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage

from .forms import FileForm
from .models import File

class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class FileListView(ListView):
    model = File
    template_name = 'file_list.html'
    context_object_name = 'files'


class UploadFileView(CreateView):
    model = File
    fields = ('title', 'xml')
    success_url = 'file_list'
    template_name = 'upload_file.html'


def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


# def file_list(request):
#     files = File.objects.all()
#     return render(request, 'file_list.html', {'files': files})


def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'upload_file.html', {
        'form': form
    })