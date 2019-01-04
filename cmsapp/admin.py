# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from cmsapp.models import Rest,Youtube_links,Images_links,News_links,Access_Token,Searched_videos,Searched_images,Testing,Upload,My_GC_Groups,Group_users_list,Keywords,Single_campaign_upload,Multiple_campaign_files,Multiple_campaign_upload,User_unique_id


class Youtube_links_Admin(admin.ModelAdmin):
    list_display = ('keyword','title','video_link','user','created_date','vid_id')

admin.site.register(Youtube_links,Youtube_links_Admin)

class Images_links_Admin(admin.ModelAdmin):
    list_display = ('keyword','title','image_link','user','created_date')

admin.site.register(Images_links,Images_links_Admin)

class News_links_Admin(admin.ModelAdmin):
    list_display = ('keyword','content','news_link','user','created_date','image')

class Access_token_Admin(admin.ModelAdmin):
    list_display  = ("ss_username","ss_client_id","ss_client_secret")

class searched_videos_links(admin.ModelAdmin):
    list_display = ('keyword','title','videos_link','video_id','created_date')

class searched_images_links(admin.ModelAdmin):
    list_display = ('keyword','title','images_link','image_id','created_date')

class Testing_admin(admin.ModelAdmin):
    list_display = ('test','ky')

class Upload_admin(admin.ModelAdmin):
    list_display = ('id','user','upload','desc','file_access_mode','file_type','group_id')

class Keywords_admin(admin.ModelAdmin):
    list_display = ('keys','upload_id')

class My_GC_Groups_admin(admin.ModelAdmin):
    list_display = ('id','group_name','group_created_by','group_created_date')


class Group_users_list_admin(admin.ModelAdmin):
    list_display = ('group_id','group_emails_list','saved_emails_date')

class Rest_admin(admin.ModelAdmin):
    list_display = ('name','age','num')

class Single_campaign_upload_admin(admin.ModelAdmin):
    list_display = ('campaign_uploaded_by','campaign_name','text_file','media_file','created_date','updated_date')

class Multiple_campaign_upload_admin(admin.ModelAdmin):
    list_display = ('id','campaign_uploaded_by','campaign_name','text_file','created_date','updated_date')

class Multiple_campaign_files_admin(admin.ModelAdmin):
    list_display = ('Multiple_campaign','mul_files',)


class User_unique_key_admin(admin.ModelAdmin):
    list_display = ('user_id','user_unique_key',)

admin.site.register( User_unique_id,User_unique_key_admin)


admin.site.register( Multiple_campaign_files,Multiple_campaign_files_admin)

admin.site.register( Multiple_campaign_upload,Multiple_campaign_upload_admin)

admin.site.register( Single_campaign_upload,Single_campaign_upload_admin)

#admin.site.register( Rest,Rest_admin)

admin.site.register( Keywords,Keywords_admin)
admin.site.register(Group_users_list,Group_users_list_admin)

admin.site.register(My_GC_Groups,My_GC_Groups_admin)

admin.site.register(Upload,Upload_admin)

#admin.site.register(Testing,Testing_admin)


admin.site.register(Searched_images,searched_images_links)

admin.site.register(Searched_videos,searched_videos_links)
#admin.site.register(Access_Token,Access_token_Admin)

admin.site.register(News_links,News_links_Admin)



