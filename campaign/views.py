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
        return render(request,'campaign/upload_file.html')

'''
 1->Invalid request
 '''
def initCampaignUpload(request):
	if(request.method == "POST"):
		return JsonResponse({'status':"in progress"});
	else :
		return JsonResponse({'statusCode':1,
			'status':"Invalid request"});