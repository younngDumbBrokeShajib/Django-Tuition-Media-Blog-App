from django.urls import path
from .views import postViews,postCreate,subjectView,contact2,PostListView,PostDetailView,PostEditView,PostDeleteView
from .views import searchView,filterView,ClassAddView
from .forms import contactForm2
#from .views import contact
from django.contrib.auth.views import LoginView
app_name='tuition'
urlpatterns = [
    #path('contact/',contact2.as_view(),name='contact'),
    path('contact2/',contact2.as_view(),name='contact2'),
    #path('contact/',contact,name="contact"),
    path('views/',postViews,name="postviews"),
    path('search/',searchView,name="searchview"),
    path('filter/',filterView,name='filter'),
    path('post/',postCreate.as_view(),name="postadd"),
    path('subview/',subjectView,name='subjectview'),
    path('list/',PostListView.as_view(),name='postlist'),
    #path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    #path('detail/<str:slug>',PostDetailView.as_view(),name='detail'),
    #path('detail/<int:id>',PostDetailView.as_view(),name='details'),
    path('detail/<int:pk>',PostDetailView.as_view(),name='detail'),
    path('edit/<int:pk>',PostEditView.as_view(),name='editpost'),
    path('delete/<int:pk>',PostDeleteView.as_view(),name='delete'),
    path('class-add/',ClassAddView.as_view(),name='class-add'),


]