from django.shortcuts import render,HttpResponse
from tuition.models import Contact
from django.views.generic import TemplateView
from django.views import View


#here to view the pages with http request all the finctions are created here
#from here we will pass the funtions to the urls.py

#to get the html file using render, use "render" then using the request pass the file in templates
#but first change in settings.py add templates directory in the templates lists.

#part-5 create a new app python manage.py startup tuition (a new folder will be created)
#now to connect the new app (tuition) go to setting.py ad add the appname in the installed app list

#part-6 now we will pass variables trhough this function to the views
#so a dictionary is being passed down with the render function


#part-09 here we will use post method for this save the values in a variable
# then inside of the POST['varibale'] add the exact name of set in the form
#use csrf token

#creating a object for model(contact form) here the first parameter for Concact(x=y)
#here the x=the field of the model class and y=the name of the varibale in the front end html input field
#now to check the users and the inputed data first create a superuser using (createsuperuser)
#then in tuituin app admin.py first import the model 
#then register the model in the admin.py file

#uses of model manager. First to return the name of this model's itself. Go to models.py and check def _str_str()
#.save() is another usage of model manaeger. here the return values will be shown in the admin panel.


#part-11 here we will transfer the views to tuition form here so go to tuition/views.py to see the documentation

def home(request):
    #return HttpResponse('Hello world')
    name=['shajib','noel','fariha']
    context={
        'name':name,
    }
    return render(request,'home.html',context)
class homeView(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['msg1']='Welcome to our homepage'
        context['msg2']='Welcome to our homepage2'
        return context






     