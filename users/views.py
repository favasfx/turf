from users.models import Users, Bookings, Feedbacks




from django.shortcuts import render,redirect

# Create your views here.
def user(request):
    return render(request,'user.html')

def index(request):
    return render(request,'index.html')


def booking(request):
    
    if request.method == 'POST':
        date = request.POST['date']
        time = request.POST['time']
        # time = request.POST['time']
        userobj = Bookings(date = date, time = time, status = "Pending", user_id = request.session['userId'])
        userobj.save()
    return render(request,'bookings.html')

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        userobj = Users(name=name, email = email, phone = phone, password = password, )
        userobj.save()
    return render(request,'login.html')

def home(request):
    if request.method == 'POST':
        feedback = request.POST['feedback']
        userobj =Feedbacks(feedback = feedback)
        userobj.save()
    return render(request,'home.html')

def signin(request):

    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']  
        try:
            user = Users.objects.get(name=email,password=password)
            # if user.email == username and user.password == password:
            request.session['userId'] = user.id
            print(request.session['userId'])
            return render(request,'home.html')

        except Exception as e:
            print(e)
            return render(request,'login.html',{'message':'Invalid Email or Password'})

    
    # print(username)
    # print(password)
    return render(request,'login.html')

def bookingstatus(request):
    session = request.session['userId']
    print(session)
    objpending = Bookings.objects.filter(user_id = session,status="Pending")
    objcompleted = Bookings.objects.filter(user_id = session,status="Completed")
    print(objcompleted)
    return render(request,'bookingstatus.html',{'users':objpending,'completed':objcompleted})

def usr_cancel_booking(request,id=0):
    Bookings.objects.get(id=id).delete()
    return redirect('bookingstatus')    