from django import forms
from .models import History

class CountForm(forms.ModelForm):
    class Meta:
        model=History
        fields=('MaTem',)
        widgets={
            'MaTem':forms.TextInput(attrs={'id':'txtCheck','name':"txtCheck" ,'type':"text",'placeholder':'Nhập mã phủ cào trên tem'}),
        }

