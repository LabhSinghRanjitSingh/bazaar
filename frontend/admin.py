from django.contrib import admin
from frontend.models import Slider,Scroller
# Register your models here.

class AdminSlider(admin.ModelAdmin):
    list_display =['mainText','subText','book']

class AdminScroller(admin.ModelAdmin):
    list_display =['tag','book']

admin.site.register(Slider,AdminSlider)
admin.site.register(Scroller,AdminScroller)
