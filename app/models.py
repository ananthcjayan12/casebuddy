from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_lawyer = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class Case(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('PENDING_PAYMENT', 'Pending Payment'),
        ('ACTIVE', 'Active'),
        ('CLOSED', 'Closed'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
    ]

    CATEGORY_CHOICES = [
        ('CIVIL', 'Civil Law'),
        ('CRIMINAL', 'Criminal Law'),
        ('FAMILY', 'Family Law'),
        ('PROPERTY', 'Property Law'),
        ('CORPORATE', 'Corporate Law'),
        ('EMPLOYMENT', 'Employment Law'),
        ('IMMIGRATION', 'Immigration Law'),
        ('INTELLECTUAL', 'Intellectual Property'),
        ('TAX', 'Tax Law'),
        ('BANKRUPTCY', 'Bankruptcy Law'),
        ('PERSONAL_INJURY', 'Personal Injury'),
        ('ESTATE', 'Estate Planning'),
        ('ENVIRONMENTAL', 'Environmental Law'),
        ('CONSTITUTIONAL', 'Constitutional Law'),
        ('OTHER', 'Other')
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_cases')
    lawyer = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='lawyer_cases',
        null=True,
        blank=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='OTHER'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    client_draft = models.TextField(blank=True)
    lawyer_draft = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.client.username}"

class CaseQuestionnaire(models.Model):
    case = models.OneToOneField(Case, on_delete=models.CASCADE, related_name='questionnaire')
    
    # Client Information
    client_name = models.CharField(max_length=200)
    client_age = models.IntegerField()
    client_address = models.TextField()
    client_phone = models.CharField(max_length=15, null=True, blank=True)
    client_email = models.EmailField(null=True, blank=True)
    
    # Defendant Information
    defendant_name = models.CharField(max_length=200, null=True, blank=True)
    defendant_address = models.TextField(null=True, blank=True)
    defendant_contact = models.CharField(max_length=15, blank=True, null=True)
    
    # Incident Details
    incident_date = models.DateField()
    incident_location = models.CharField(max_length=200)
    incident_description = models.TextField()
    
    # Witness Information
    witnesses = models.TextField(blank=True, help_text="Enter each witness's name, address, and contact information")
    
    # Legal Information
    court_jurisdiction = models.CharField(max_length=200, help_text="Specify the court where the case will be filed", null=True, blank=True)
    case_number = models.CharField(max_length=50, blank=True, help_text="If any previous case number exists")
    previous_legal_actions = models.TextField(blank=True)
    desired_outcome = models.TextField()
    additional_info = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Questionnaire for {self.case.title}"

class Payment(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for case: {self.case.title}"
