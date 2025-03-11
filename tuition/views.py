import form
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Contact,Post,Subject,Class_in,User
from .forms import contactForm,PostForm,contactForm2,ClassAddForm
from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView,UpdateView,DeleteView
from django.views.generic import CreateView
from django.contrib import messages
from django.db.models import Q

from session.models import UserModel

# Create your views here.
#----------------part 11--------------------
#here we have copied the views
#and for else block if the url is hit fro m get method 
#import he contactfrom class too and the models and i
#now just remove all the content from the html page of contact.html and replace with {{form}}
#need to change the url, new file under tuition app urls.py and import the views of tuition app
#then in the main project urls.py file add include with 'tuition' urls so that
#we can hit 'tuition/contact' url and the contact url is located inside the tuition app urls.py file

#then


def searchView(request):
    query=request.POST.get('search','')
    if query:
        query_set=(Q(title__icontains=query)) | (Q(details__icontains=query)) | (Q(medium__icontains=query)) | (Q(subject__name__icontains=query))
        results=Post.objects.filter(query_set).distinct()
        print("Query:", query)
        print("results",results)

    else:
        results=[]
    context={
        'results':results,
        }
    return render(request,'tuition/search.html',context)

def filterView(request):
    if request.method=='POST':
        #first get the data from the fron-end using html field name from postlist.html
        subjects = request.POST.get('subject', None)
        class_in = request.POST.get('class', None)
        avail = request.POST.get('availability', None)
        salarylow = request.POST.get('salary_from', None)
        salaryhigh = request.POST.get('salary_to', None)
        if subjects or class_in:
            query_set=Q(subject__name__icontains=subjects)|Q(class_in__name__icontains=class_in)
            results=Post.objects.filter(query_set).distinct()
            if avail:
                results=results.filter(available=True)
            if salarylow:
                results=results.filter(salery__gte=salarylow)
            if salaryhigh:
                results=results.filter(salery__lte=salaryhigh)
    else:
        results=[]
    context={
        'results':results
    }
    return render(request,'tuition/search.html',context)



class contact2(View): #import django.views
    form_name=contactForm2
    template_name='contactform2.html'
    def get(self,request,*args,**kwargs):
        form=self.form_name()
        return render(request,'contactform2.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=self.form_name(request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request,"Form Successfully Saved")
            #return HttpResponse("Success")
#The reverse_lazy function returns a string representation of the URL (or a proxy object for a URL in some cases) but does not inherently handle HTTP responses.
#so we need to use HttpResponseRedirect(reverse_laxy("tuition:postlist"))

            return HttpResponseRedirect(reverse_lazy('tuition:postlist'))

        return render(request,'contactform2.html',{'form':form})

# def contact(request):
#     if request.method=='POST':
#         form=contactForm(request.POST)
#         #to save it from  just a html field use request.POST['html_field_name']
#
#         #here if we remove the precedding coma after name=request.POST['name'] then we can create a perfect type of values
#         if form.is_valid():
#
#             name=form.cleaned_data['name'] #here value inside [] is the varr name of the forms.py
#             phone=form.cleaned_data['phone']
#             content=form.cleaned_data['content']
#             print(name)
#             print(type(name))
#             obj=Contact(name=name,phone=phone,content=content) #creating an object of Contact model class
#             obj.save()
#     else:
#         form=contactForm()
#     return render(request,'contact.html',{'form':form})




def postViews(request):
    post=Post.objects.all()
    
    return render(request,'tuition/postview.html',{'post':post})

class ClassAddView(View):
    form_name=ClassAddForm
    template_name='tuition/classadd.html'

    def post(self,request,*args,**kwargs):
        form=self.form_name(request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request, "Form Successfully Saved")
            return HttpResponseRedirect(reverse_lazy('tuition:postlist'))
        return render(request, 'tuition/classadd.html', {'form': form})
    def get(self,request):
        form=self.form_name()
        return render(request,'tuition/classadd.html',{'form':form})


def subjectView(request):
    #sub=Subject.objects.all() to get all the objects
    sub=Subject.objects.get(name="Maths") #to get the eexact object of having name=Maths
    post=sub.Subjects_added.all() #Subjects_added is the related name in Post Model
    return render(request,'tuition/subjectview.html',{'sub':sub,'post':post})

#to use createView generic class import the view first

class postCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'tuition/postadd.html'
    #success_url = '/'

    #for success url we need to override a function first which is built-in for CreateView class view
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('tuition:subjectview') #tuition is the appname mentioned in urls.py and subjectview is the url name




# def postCreate(request):
#     if request.method=="POST":
#         form=PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             obj=form.save(commit=False)
#             obj.user=request.user
#             obj.save()
#             sub=form.cleaned_data['subject']
#             cls_in=form.cleaned_data['class_in']
#             sec=form.cleaned_data['']
#             for i in sub:
#                 obj.subject.add(i)
#                 obj.save()
#             for j in cls_in:
#                 obj.class_in.add(j)
#                 obj.save()
#             return HttpResponse("Success")
#     else:
#         form=PostForm()
#     return render(request,'tuition/postadd.html',{'form':form})
class PostListView(ListView): #immport list view package
    model=Post #to get all the Post objects without any filter
    # = Post.objects.filter(user=1) # to filter the post objects.
    template_name = 'tuition/postlist.html'
    context_object_name = "postlist" #this is used in the for loop
    #query_set=Post.objects.filter(user=1)
    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['postlist']=context.get('object_list') #this renames the object_list into postlist to use in front end
        context['msg']='This is context message'
        context['subjects']=Subject.objects.all() #used in filter
        context['class_in']=Class_in.objects.all() #this is to send the subject objects in fron-end dropdown list
        return context

class PostDetailView(DetailView):
    model=Post
    template_name = 'tuition/detail.html'
    context_object_name = 'postdetail'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post=self.get_object()
        print("Logged-in user:", self.request.user)
        print("Post author:", post.user)
        context['author']=self.request.user == post.user #acts as a boolean in fron-end to check if the user is authenticated
        return context
class PostEditView(UpdateView):
    model=Post
    template_name='tuition/postadd.html'
    form_class = PostForm
    def get_success_url(self):
        id=self.object.id
        return reverse_lazy('tuition:detail',kwargs={'pk':id})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post=self.get_object()
        print("Logged-in user:", self.request.user)
        print("Post author:", post.user)
        context['author']=self.request.user == post.user
        return context

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'tuition/delete.html'
    success_url = reverse_lazy('tuition:postlist')

def get_vipView(request):
    vip=UserModel.vip_author.get_vip_cus()
    for user in vip:
        print(user)