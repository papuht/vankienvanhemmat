from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(label = 'Viesti', widget=forms.Textarea(), max_length=4000, help_text='Viestin maksimipituus 4000 merkkiä')
    subject = forms.CharField(label = 'Otsikko', max_length=200)
    class Meta:
        model = Topic
        fields = ['subject', 'message']
		
		
class PostForm(forms.ModelForm):
    message = forms.CharField(label = 'Viesti', widget=forms.Textarea(), max_length=4000, help_text='Viestin maksimipituus 4000 merkkiä')
    class Meta:
        model = Post
        fields = ['message', ]