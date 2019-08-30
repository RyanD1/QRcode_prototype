from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from .forms import ExcelForm
from .models import ExcelFile
from excel_upload import excel_parser
# Create your views here.


class Home(TemplateView):
    template_name = 'excel_upload/home.html'


def upload_successful(request):
    return render(request, 'excel_upload/upload_successful.html')


def upload_failed(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            newExcel = ExcelFile(excel=request.FILES['excel'])
            newExcel.save()
            workbook = excel_parser.verifyExcel(settings.BASE_DIR + newExcel.excel.url)
            if not workbook:
                newExcel.delete()
                return redirect('excelupload-failed')
            if not excel_parser.verifyTemplate(workbook):
                newExcel.delete()
                return redirect('excelupload-failed')
            return redirect('excelupload-successful')
        else:
            return redirect('excelupload-failed')
    else:
        form = ExcelForm()

    return render(request, 'excel_upload/upload_failed.html', {
        'form': form
    })


def upload(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            newExcel = ExcelFile(excel=request.FILES['excel'])
            newExcel.save()
            workbook = excel_parser.verifyExcel(settings.BASE_DIR + newExcel.excel.url)
            if not workbook:
                newExcel.delete()
                return redirect('excelupload-failed')
            if not excel_parser.verifyTemplate(workbook):
                newExcel.delete()
                return redirect('excelupload-failed')
            return redirect('excelupload-successful')
        else:
            return redirect('excelupload-failed')
    else:
        form = ExcelForm()

    return render(request, 'excel_upload/upload.html', {
        'form': form
    })
    # if request.method == 'POST':
    #     form = ExcelForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('upload_successful')
    # else:
    #     form = ExcelForm()
    # return render(request, 'upload.html', {
    #     'form': form
    # })
    # if request.method == 'POST':
    #     form = DocumentForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('')
    # uploaded_file = request.FILES['uploadedfile']
    #     fs = FileSystemStorage()
    #     fs.save(uploaded_file.name, uploaded_file)
    #     if excel_parser.verifyExcel(uploaded_file):
    #         print("Upload Successful")
    #         return render(request, 'excel_upload/upload_successful.html')
    #     else:
    #         print("Upload Failed")
    #         return render(request, 'excel_upload/upload_failed.html')
    # return render(request, 'excel_upload/home.html')


# def upload(request):
#     # if request.method == 'POST':
#     #     uploaded_file = request.FILES['uploadedfile']
#     #     fs = FileSystemStorage()
#     #     fs.save(uploaded_file.name, uploaded_file)
#     #     if excel_parser.verifyExcel(uploaded_file):
#     #         print("Upload Successful")
#     #         return render(request, 'excel_upload/upload_successful.html')
#     #     else:
#     #         print("Upload Failed")
#     #         return render(request, 'excel_upload/upload_failed.html')
#     # return render(request, 'excel_upload/home.html')
