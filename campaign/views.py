from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from cmsapp.models import Multiple_campaign_upload

# Create your views here.
def upload_camp_web(request):
    if request.method == "POST":
        #fileObj = request.FILES['file']
        campaigns = Multiple_campaign_upload.objects.filter();
        campaigns = list(campaigns);
        return JsonResponse({'file':'fileObj.size'})
    else:
        campaigns = Multiple_campaign_upload.objects.filter(campaign_uploaded_by=1);
        campaigns = list(campaigns.values());
        
        return JsonResponse({'campaigns':campaigns});
        #return render(request,'campaign/upload_file.html')
