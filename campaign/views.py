from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from cmsapp.models import Multiple_campaign_upload
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from .models import CampaignInfo
# Create your views here.
@login_required
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
 2->Invalid session, please login
 3->Unable to save the campaign
 '''
@api_view(['GET','POST'])
def initCampaignUpload(request):
    if(request.method == "POST" and
     'campaign' in request.POST and 'size' in request.POST):
        #check the request whether from web or app
        accessToken = request.POST.get('accessToken');
        if(accessToken == "web"):
            if request.user.is_authenticated:
                response = CampaignInfo.processInfoAndSaveCampaign(request.POST.get('info'),
                    accessToken,request.user.id,
                    request.POST.get('campaign'),request.POST.get('size'));
                return JsonResponse(response);
            else:
               return JsonResponse({'statusCode':2,
                    'status':'Invalid session, please login'});
        else:
            response = CampaignInfo.processInfoAndSaveCampaign(request.POST.get('info'),
                    "api",accessToken,request.POST.get('campaign'),request.POST.get('size'));
            return JsonResponse(response);
    else :
        return JsonResponse({'statusCode':1,
            'status':"Invalid request"});