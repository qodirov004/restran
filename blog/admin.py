from django.contrib import admin
from .models import BannerStage, ServiceStar, Contact, TeamStage , MenuItem, Category, BookingStage, BookingMedia, Orders

admin.site.register(Contact)
admin.site.register(BookingStage)
admin.site.register(BookingMedia)
admin.site.register(Orders)









@admin.register(BannerStage)
class Banner(admin.ModelAdmin):
    list_display = ('title', 'subtitle')

    def has_add_permission(self, request):
        if BannerStage.objects.count() >= 1:
            return False
        else:
            return True
        
@admin.register(ServiceStar)
class Service(admin.ModelAdmin):
    list_display = ('title', 'image', 'body')

    def has_add_permission(self, request):
        if ServiceStar.objects.count() >= 4:
            return False
        else:
            return True
        
@admin.register(TeamStage)
class Team(admin.ModelAdmin):
    list_display = ('name', 'image', 'subject', 'facebook', 'telegram', 'instagram')

    def has_add_permission(self, request):
        if TeamStage.objects.count() >= 8:
            return False
        else:
            return True

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')