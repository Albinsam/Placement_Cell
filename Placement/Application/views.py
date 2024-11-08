from django.shortcuts import render,redirect
from .forms import JobApplicationForm
from django.contrib.auth import logout as auth_logout
from .forms import SearchForm
from Student.models import Student  # Adjust this import based on your model
from . models import Job
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

def jobs(request):
    return render(request,'Jobs.html')

def app(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save form data to the database
            return redirect('index')  # Redirect to a success page
    else:
        form = JobApplicationForm()
    
    return render(request, 'Application.html', {'form': form})

def logout(request):
    # Call Django's built-in logout function to clear the session and log out the user
    auth_logout(request)
    
    return redirect('home')


def search_view(request):
    form = SearchForm(request.GET or None)
    results = None

    if form.is_valid() and form.cleaned_data['query']:
        query = form.cleaned_data['query']
        # Search across job_title, skill, and company_name
        results = Job.objects.filter(
            Q(job_title__icontains=query) |  # type: ignore
            Q(skill__icontains=query) |  # type: ignore
            Q(company_name__icontains=query) # type: ignore
        )

    return render(request, 'Jobs.html', {'form': form, 'results': results})