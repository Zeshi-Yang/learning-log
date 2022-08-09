from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:        
        model=Topic
        fields=['text','public']
        labels={'text':'','public':''}
    public=forms.BooleanField(required=False)

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields=['text']
        labels={'text':''}
        widgets={'text':forms.Textarea(attrs={'cols':80})}

class PublicForm(forms.ModelForm):
    class Meta:
        public=forms.BooleanField()
        model=Topic
        exclude=()