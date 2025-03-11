from django import forms
from django.forms import Form

from .models import Contact,Post,Class_in


class contactForm(forms.Form):
    #to use this from create an object in the views.py within the POST method
    name=forms.CharField(max_length=100, required=True,label="Your name")
    phone=forms.CharField(max_length=100,required=True,label="Your phone")
    content=forms.CharField(max_length=1000,required=True,label="Content")
class contactForm2(forms.ModelForm):
    # to use this from create an object in the views.py within the POST method
    class Meta:
        model=Contact
        fields='__all__'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].initial='My Name initial'
        self.fields['content'].initial='This is content'
    def clean_name(self):
        value=self.cleaned_data.get('name')
        count_word=value.split(' ')
        if len(count_word)>3:
            raise forms.ValidationError('Name cannot be more than 3 words')
        else:
            return value
        # widgets={
        # 'name':forms.TextInput(attrs={'class':'form-control'}),
        # 'phone':forms.TextInput(attrs={"class:'form-control"}),
        # 'content':forms.Textarea(attrs={'class':'form-control'})
        # }
        # labels={
        #     'name':"Full Name",
        #     'phone':'Phone NO',
        #     'content':'Content'
        # }

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['user','id','slug']
        widgets={
            'subject':forms.CheckboxSelectMultiple(attrs={
                'multiple':True,
            }),
            'class_in':forms.CheckboxSelectMultiple(
                {
                    'multiple':True,
                }
            )
        }

class ClassAddForm(forms.ModelForm):
    class Meta:
        model=Class_in
        fields='__all__'
