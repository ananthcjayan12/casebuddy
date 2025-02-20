from django.contrib import admin
from .models import UserProfile, Case, Payment

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_lawyer', 'phone_number')
    list_filter = ('is_lawyer',)
    search_fields = ('user__username', 'phone_number')

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'lawyer', 'status', 'payment_status', 'created_at')
    list_filter = ('status', 'payment_status')
    search_fields = ('title', 'client__username', 'lawyer__username')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('case', 'amount', 'is_paid', 'payment_date')
    list_filter = ('is_paid',)
    search_fields = ('case__title',)
