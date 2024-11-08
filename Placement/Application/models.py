from django.db import models

# Create your models here.
class JobApplication(models.Model):
    job_name = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/', blank=False, null=False)  # For storing resume files
    cover_letter_text = models.TextField(blank=True, null=True)  # Optional cover letter text
    cover_letter_file = models.FileField(upload_to='cover_letters/', blank=True, null=True)  # Optional cover letter file

    def __str__(self):
        return f"{self.job_name} "
    
class Job(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='company_images/')
    created_date = models.DateTimeField(auto_now_add=True)
    skill = models.CharField(max_length=255)
    description = models.TextField(default="No description provided.")  

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"