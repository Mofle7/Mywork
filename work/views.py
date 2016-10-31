from django.shortcuts import render, get_object_or_404
from django.forms import modelformset_factory
from work.models import Adv, Profile
from django.forms import ModelForm


def main():
    pass
def home():
    pass
def support():
    pass
def about_us():
    pass



def show_adv():
    return True


class AdvForm(ModelForm):
    class Meat:
        model = Adv
        fields = ['adv_text']

def add_adv(requset, pk):
    if requset.method == 'POST':
        instance = Adv (user = user)
        form = AdvForm(requset.POST, instance = instance)
        if form.is_valid :
            form.save()
    else:
        form = AdvForm
    return render (requset,add_adv.html,{"form":form})
    return HttpResponseRedirect(reverse('show_adv'))

def edit_adv(requset, pk):
    if requset.method == 'GET':
        added_adv = Adv (user='user', adv_text='adv_text')
        form = AdvForm (requset.POST, instance=added_adv)
        if form.is_valid:
            form.save()
    else :
        form = AdvForm
    return render (requset,edit_adv.html,{"form":form})
    return HttpResponseRedirect(reverse('edit_adv'))
def del_adv():
    pass



def show_profile():
    pass
def add_profile(requset,pk):
    if requset.method == 'POST':
        instance = Profile (user = 'user')
        form = ProfileForm(requset.POST, instance = instance)
        if form.is_valid :
            form.save()
    else:
        form = ProfileForm
    return render (requset,add_adv.html,{"form":form})
    return HttpResponseRedirect(reverse('show_profile'))

def edit_profile(requset, pk):
    if requset.method == 'GET':
        added_profile = Profile (user='user',name='name', mobile='mobile')
        form = ProfileForm (requset.POST, instance=added_profile)
        if form.is_valid:
            form.save()
    else :
        form = ProfileForm
    return render (requset,edit_profile.html,{"form":form})
    return HttpResponseRedirect(reverse('show_profile'))
def del_profile():
    pass



def search_page():
    pass
def forget_password():
    pass
# Create your views here.
# Create your views here.
