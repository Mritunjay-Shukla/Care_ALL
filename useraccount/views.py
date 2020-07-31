from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render
from django.contrib.auth import get_user_model
from useraccount.forms import SignupForm 
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.views import generic
from useraccount.models import Profile, Addfriend, Review
from django.http import HttpResponse
from useraccount.forms import profileform
# Create your views here.

class Signup(CreateView):
    model = settings.AUTH_USER_MODEL
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = '/'

    def form_valid(self, form): 
        to_return = super().form_valid(form)
        login(self.request, self.object)
        return to_return

class Profileupdate(generic.UpdateView):
    model = get_user_model()
    #fields = ('first_name', 'last_name', 'email', 'phone_number', 'location', 'fees', 'pic', 'user_type', 'bio',)
    #pk_url_kwarg = 'pk'
    form_class = profileform
    template_name = 'registration/profile_update.html'
    success_url = "/"

def Userdetailpage(request, id):   
    profile = get_user_model().objects.get(id = request.user.id)
    pro = Profile.objects.get(user=request.user)
    rec_rest = Addfriend.objects.all()
    f = pro.friends.all()
    l = []
    for i in f:
        if not(i.fees == None):
            l.append(i.fees)
    earning = sum(l)        
    return render(request, "registration/user.html",context = {"profile":profile, 'pro':pro, "rec_rest":rec_rest, "earning":earning})

def sendrequest(request, id):
    reciever = Profile.objects.get(user__id = id)
    user = request.user.id
    sender = Profile.objects.get(user__id = user)
    if sender.user.user_type == 'CT' and sender.friends.count() == 1:
        return HttpResponse("Sorry you have exceed your limit.")
    elif sender.user.user_type == 'CG' and sender.friends.count() == 4:
        return HttpResponse("Sorry you have exceed your limit.")
    friend_obj = Addfriend.objects.create(sender=sender, reciever=reciever)
    return redirect('/')

def deletereuest(request, id):
    rec_rest = Addfriend.objects.get(id=id)
    print(rec_rest)
    rec_rest.delete()
    idd = request.user.id
    return redirect("userdetail/{}".format(idd))


def acceptreuest(request, id):
    rec_rest = Addfriend.objects.get(id=id)
    u = rec_rest.sender
    r = rec_rest.reciever
    u.friends.add(rec_rest.reciever.user)
    r.friends.add(rec_rest.sender.user)
    u.save()
    r.save()
    rec_rest.delete()
    idd = request.user.id
    return redirect("userdetail/{}".format(idd))

def addreview(request, **kwargs):
    rating = request.POST.get('rating')
    review_sms = request.POST.get('review')
    to_user = get_user_model().objects.get(id=kwargs.get('id'))
    chk_rat = Review.objects.filter(to_user=to_user)
    for i in chk_rat:
        if request.user == i.from_user:
            return HttpResponse('Thanks..You have already submitted your review.')
    review = Review.objects.create(to_user = to_user, review = review_sms, from_user = request.user, rating= rating)
    return redirect('detail/{}'.format(kwargs.get('id')))