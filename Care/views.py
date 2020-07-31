from django.shortcuts import render, redirect
from django.views import View
from django.views import generic
from django.conf import settings
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormView, CreateView
from useraccount.models import Profile, Review
#from useraccount.models import Gig
# Create your views here.

class HomePage(generic.ListView):
    model = get_user_model()
    context_object_name = 'profile'
    queryset = get_user_model().objects.filter(user_type = 'CG')
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prof = get_user_model().objects.filter(user_type = 'CT')
        context['prof'] = prof
        return context


def detailpage(request, id):
    data = get_user_model().objects.get(id = id)
    prof = Profile.objects.get(user=request.user)
    profdata = prof.friends.all()
    rating = Review.objects.filter(to_user=data)
    print(rating)
    if rating:
        l = []
        for rat in rating:
            l.append(rat.rating)
        tr = len(l)
        gr = sum(l)
        fr = gr/tr
        fr = round(fr, 1)
        return render(request, "detail.html", context={"data":data, "profdata":profdata, "fr":fr, "rating":rating})
    return render(request, "detail.html", context={"data":data, "profdata":profdata})
