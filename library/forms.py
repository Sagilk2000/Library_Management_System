# from  django.shortcuts import render,redirect
# from django.template.context_processors import request
#
# from .forms import UploadFileForm
#
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return
#         redirect('success_view_name')
#     else:
#         form = UploadFileForm()
#         return render(request, 'upload.html', {'form': form})
