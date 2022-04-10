from functools import wraps
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from formwizard.forms import LoginForm, step1, step2, step4, step3, step4, step5
from django.contrib.auth import login, authenticate, logout

# check if user is not logged
def is_not_logged_in(f):
    @wraps(f)
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated == False:
            return f(request, *args, *kwargs)
        else:
            return redirect('wizard:dashboard')
    return wrap

# check if user is logged
def is_logged_in(f):
    @wraps(f)
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated == True:
            return f(request, *args, *kwargs)
            
        else:
           return redirect('wizard:login')
            

    return wrap

# Create your views here.
@is_not_logged_in
def Home(request):
    #if form is submitted
    if request.method == 'POST':
        # recieve all data from the form
        title = request.POST.get('title', None)
        bidding_settings = request.POST.get('bidding_settings', None)
        company_name = request.POST.get('company_name', None)
        birth_date = request.POST.get('birth_date', None)
        home_address = request.POST.get('home_address', None)
        username = request.POST.get('username', None)
        
        phone_number = request.POST.get('phone_number', None)
        google_ads_account_ID = request.POST.get('google_ads_account_ID', None)
        firstname = request.POST.get('first_name', None)
        lastname = request.POST.get('last_name', None)
        emaill = request.POST.get('email_address', None)
        password1 = request.POST.get('password', None)

        # print(firstname, lastname, emaill, password1, title, bidding_settings, company_name, birth_date, home_address, google_ads_account_ID)
        
        # check if user exists
        if User.objects.filter(email=emaill).exists():
            messages.add_message(request, messages.SUCCESS, 'email already in use')
            return redirect('wizard:home')
        elif User.objects.filter(username=username).exists():
            messages.add_message(request, messages.SUCCESS, 'username already in use')
            return redirect('wizard:home')

        # create user instance
        user = User.objects.create(
            first_name = firstname,
            username=username,
            last_name = lastname,
            email = emaill,
            password = make_password(password1),
        )
        

        user =  User.objects.get(email=emaill,)
        profile = user.profile # because of signal and one2one relation
        # saving user profile data 
        profile.title = title
        profile.address = home_address
        profile.company_name = company_name
        profile.dob = birth_date
        profile.bid_settings = bidding_settings
        profile.googleId = google_ads_account_ID
        profile.phone = phone_number

        profile.save()
        
        # authenticate the user
        user = authenticate(username=username, password=password1)

        # login the user then redirect to dashboard
        login(request, user)

        return redirect('wizard:dashboard')
    else:
        context ={}
        context['step1']= step1()
        context['step2']= step2()
        context['step3']= step3()
        context['step4']= step4()
        context['step5']= step5()
        return render(request, 'mfw1.html', context)

@is_not_logged_in
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password1 = request.POST.get('password', None)
        print(username,password1)

        # check if username exists in database
        if not User.objects.filter(username=username).exists():
            messages.add_message(request, messages.SUCCESS, 'user does not exists')
            print('not exist')
            return redirect('wizard:login')

        #  authenticate the user, login and redirect
        user = authenticate(username=username, password=password1)
        login(request, user)
        return redirect('wizard:dashboard')
    context ={}
    context['form']= LoginForm()
    return render(request, 'login.html', context)

# Dashboard view
def Dashboard(request):
    return render(request, 'dashboard.html', )


# Login request view
def logout_request(request):

    logout(request)
    

    return redirect('wizard:login')
