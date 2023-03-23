from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='제목'),


    superv = forms.CharField(label='감독'),


    content = forms.CharField(label='코멘트')


    class Meta:
        model = Article
        fields = '__all__'



