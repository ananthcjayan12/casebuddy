from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('case/submit/', views.submit_case, name='submit_case'),
    path('cases/', views.case_list, name='case_list'),
    path('case/<int:pk>/', views.case_detail, name='case_detail'),
    path('case/<int:case_id>/payment/', views.make_payment, name='make_payment'),
    path('payment/<int:payment_id>/success/', views.payment_success, name='payment_success'),
    path('accounts/profile/', views.profile, name='profile'),
    path('cases/available/', views.available_cases, name='available_cases'),
    path('case/<int:pk>/accept/', views.accept_case, name='accept_case'),
    path('case/<int:pk>/questionnaire/', views.case_questionnaire, name='case_questionnaire'),
    path('case/<int:pk>/generate-draft/', views.generate_draft, name='generate_draft'),
    path('case/<int:pk>/download-draft/', views.download_draft, name='download_draft'),
] 