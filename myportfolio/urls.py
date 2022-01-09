from django.urls import path
from django.views.static import serve
from . import views
from django.conf.urls import url,include
from portfolio.settings import STATICFILES_DIRS

urlpatterns =[

    path("",views.index,name="index"),
    path("projects",views.projects,name="projects"),
    path("experiences",views.experiences,name="experiences"),
    path("blogs",views.blogs,name="blogs"),
    path("contact",views.contact,name="contact"),

]