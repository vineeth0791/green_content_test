from django.shortcuts import render

# Create your views here.
def upload_camp_web(request):
    if request.method == "POST":
        #fileObj = request.FILES['file']
        return JsonResponse({'file':'fileObj.size'})
    else:
        
        return render(request,'campaign/upload_file.html')
