"""mywork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from work import urls as work_urls
from django.conf import settings
from django.conf.urls.static import static
from work.views import ProfileSignupForm
from userena import views as userena_views


urlpatterns=[
url(r'^admin/', admin.site.urls),
url(r'', include(work_urls)),
url(r'^accounts/', include('userena.urls')),
url(r'^signup/$', userena_views.signup,{'signup_form': ProfileSignupForm, 'template_name': 'userena/profile_signup_form.html'},name='signup'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
