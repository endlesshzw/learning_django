from django import  forms

from .models import Topic, Entry, Info

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets ={'text': forms.Textarea(attrs={'cols':80})}

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info