from django.shortcuts import render, get_object_or_404
from django.forms import modelformset_factory
from work.models import Adv, Profile, Worker
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from userena.forms import SignupForm


def main(requset):
    advs = Adv.objects.all()
    workers = Worker.objects.all()
    return render(requset,'work/main.html',{'advs':advs},{'workers':workers})

def support(requset):
    return render(requset,'work/support.html',)

def about_us(requset):
    return render(requset,'work/about.html',)

#############################

def show_adv(requset, pk):
    adv = get_object_or_404(Adv, pk=pk)
    return render (requset,'work/show_adv.html',{'adv':adv})

def add_adv(requset):
    if requset.method == 'POST':
        instance = Adv (user = requset.user)
        form = AdvForm(requset.POST, instance = instance)
        if form.is_valid :
            adv = form.save()
            return HttpResponseRedirect(reverse('show_adv',args=(adv.pk,)))
    else:
        form = AdvForm()
    return render (requset,'work/add_adv.html',{"form":form})


def edit_adv(requset, pk):
    adv = get_object_or_404(Adv, pk=pk)
    if requset.method == 'POST':
        form = AdvForm (requset.POST, instance=adv)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('edit_adv'))
    else :
        form = AdvForm(instance=adv)
    return render (requset,'work/edit_adv.html',{"form":form})


def del_adv():
    pass

################

def show_profile(requset,pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render (requset,'work/show_profile.html',{'profile':profile})

def add_profile(requset):
    if requset.method == 'POST':
        instance = Profile (user = requset.user)
        form = ProfileForm(requset.POST, instance = instance)
        if form.is_valid :
            form.save()
            return HttpResponseRedirect(reverse('show_profile'))
    else:
        form = ProfileForm()
    return render (requset,'work/add_profile.html',{"form":form})


def edit_profile(requset, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if requset.method == 'POST':
        form = ProfileForm (requset.POST, instance=profile)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('show_profile'))
    else :
        form = ProfileForm(instance=profile)
    return render (requset,'work/edit_profile.html',{"form":form})

def del_profile():
    pass



def search_page():
    pass
def forget_password():
    pass

### Models Form ###

class AdvForm(ModelForm):
    class Meta:
        model = Adv
        fields = ['adv_text']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','mobile']

class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = ['image','worker_services', 'worker_experince']

class ProfileSignupForm(SignupForm):
    class meta :
        model = Profile
        fields = ['name','mobile']

# Create your views here.
# Create your views here.
