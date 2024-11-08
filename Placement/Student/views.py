from django.shortcuts import render,redirect
from .models import Student
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import check_password
from .forms import RegistrationForm 
from .forms import LoginForm
from .models import LoginRecord # Import the LoginRecord model
from django.contrib.auth import logout as auth_logout
from django.utils.timezone import now  # Import to handle time correctly
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')


def reg1(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('login')  # Redirect to a success page or login
    else:
        form = RegistrationForm()  # For GET requests, instantiate an empty form

    return render(request, 'reg3.html', {'form': form})  # Render the form



from django.contrib import messages

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']  # Make sure to extract email here
            password = form.cleaned_data['password']

            try:
                # Retrieve the user by email
                user = Student.objects.get(email=email)

                # Check the password
                if check_password(password, user.password):  # Check against hashed password
                    # Store user information in session
                    request.session['user_id'] = user.id  # Store user ID in session
                    request.session['user'] = user.full_name  # Optional: store the user's name
                    
                    # Log the login attempt
                    LoginRecord.objects.create(
                        email=user.email,
                        login_time=now()  # Use current timestamp
                    )
                    
                    # Redirect to home after successful login
                    return redirect('index')  # Change 'home' to the name of your home page URL
                else:
                    messages.error(request, 'Invalid email or password.')
            except Student.DoesNotExist:
                messages.error(request, 'Invalid email or password.')
    else:
        form = LoginForm()  # For GET requests, instantiate an empty form

    return render(request, 'login.html', {'form': form})  # Render the login template


def logout(request):
    # Call Django's built-in logout function to clear the session and log out the user
    auth_logout(request)
    
    return redirect('home')

