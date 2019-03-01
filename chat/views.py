from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, User
from django.contrib.auth import login, logout
from .models import Message
from django.http import JsonResponse, HttpResponse
import pdb
#from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    #pdb.set_trace()
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request,user)
            return redirect('all_user')
    form = AuthenticationForm()
    #pdb.set_trace()
    return render(request, 'login.html',{'form': form})

def register(request):
    #pdb.set_trace()
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect('all_user')
    form = UserCreationForm()
    #pdb.set_trace()
    return render(request, 'register.html', {'form':form})

def all_user(request):
    #pdb.set_trace()
    user= User.objects.all()
    #pdb.set_trace()
    return render(request, 'user.html', {'user_list': user})

def chat(request, id):
    #pdb.set_trace()
    user= request.user
    receiver= User.objects.get(id=id)
    chat_sender= Message.objects.filter(sender= user, receiver= receiver)
    chat_receiver= Message.objects.filter(sender= receiver, receiver= user)
    data={
            'receiver':User.objects.get(id=id),
            'sender': request.user
            }
    #pdb.set_trace()
    return render(request, 'chat.html', {'data': data, 'chat_sender': chat_sender, 'chat_receiver': chat_receiver})

def logout_view(request):
    #pdb.set_trace()
    logout(request)
    #pdb.set_trace()
    return redirect('login')

def com(request):
    #pdb.set_trace()
    sender= request.user
    receiver= User.objects.get(username= request.POST.get('receiver'))
    chat= request.POST.get('msg')
    #return HttpResponse("Reached Messge")
    Message.objects.create(receiver= receiver, sender= sender, chat_message = chat)
    #pdb.set_trace()
    return JsonResponse('hit', safe= False)

def receive_data(request):
    #pdb.set_trace()
    user=request.user
    receiver = User.objects.get(username=request.POST.get('receiver'))
    a= Message.objects.filter(receiver=user, sender=receiver).last()
    data={'id':a.id,'chat':a.chat_message}
    #pdb.set_trace()
    return JsonResponse(data)