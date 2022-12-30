from django.shortcuts import render,redirect
from users.models import Bookings,Feedbacks
from django.http import JsonResponse



# Create your views here.
def login(request):
        if request.method == 'POST':
            email = request.POST['username']
            password = request.POST['password']  
        try:
            # user = Users.objects.get(name=email,password=password)
            if email == 'admin' and password == '123':
                request.session['userId'] = 1
                print(request.session['userId'])
                return redirect('dashboard')

        except Exception as e:
            print(e)
            return render(request,'login.html',{'message':'Invalid Email or Password'})
        return render(request,'admin_login.html')

def booking(request):
    return render(request,'bookings.html')

def dashboard(request):
    return render(request,'dashboard.html')

def feedbacks(request):
    obj = Feedbacks.objects.all()
    return render(request,'feedbacks.html',{'data':obj})

def messages(request):
    return render(request,'messages.html')

def pending_bookings(request):
    obj = Bookings.objects.filter(status='Pending')
    return render(request,'pending_bookings.html',{'data':obj})

def service_history(request):
    return render(request,'service_history.html')

def total_booking(request):
    obj = Bookings.objects.all()
    if request.method == 'POST':
            uid=request.POST['id']
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            date = request.POST['date']
            time = request.POST['time']
            status = request.POST['status']
            # time = request.POST['time']
            Bookings.objects.filter(id=uid).update(name=name, email = email, phone = phone, date = date, time = time, status = status  )
    return render(request,'total_booking.html',{'bookings':obj})

def completed_booking(request):
    obj = Bookings.objects.filter(status='Completed')
    return render(request,'completed_booking.html',{'data':obj})

def edit_bookings(request):
    id = request.POST.get('id')
    print(id)
    datas = Bookings.objects.get(id=id)
    # model_to_dict(data)
    #print(data.car_name)
    data={'id': datas.id,'name':datas.name,'phone':datas.phone,'email':datas.email,'date':datas.date,'time':datas.time,'status':datas.status}
    return JsonResponse({'data': data})

def cancelFeedback(request,id=0):
    print("Helloooo")
    Feedbacks.objects.get(id=id).delete()
    return redirect('feedbacks')

def cancelBooking(request,id=0):
    print("Helloooo")
    Bookings.objects.get(id=id).delete()
    return redirect('total_booking')

