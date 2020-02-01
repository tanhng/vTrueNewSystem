from django import forms
from .models import vtrueUser

tinhthanh_choices=[('1','Hanoi'),('2','Da Nang')]

class DoanhNghiepForm(forms.ModelForm):
    class Meta:
        model=vtrueUser
        fields=('TenDN','DiaChiDangkyKD','matinhthanh','TenNguoiDaiDien','TenTK','DienThoaiNguoiDaiDien')
        widgets={
            'TenDN':forms.TextInput(attrs={'id':'Text4','name':"TenDN" ,'type':"text", 'size':"60", 'maxlength':"200"}),
            'DiaChiDangkyKD':forms.TextInput(attrs={'name':"DiaChiDangkyKD", 'type':"text", 'size':"60", 'maxlength':"200", 'id':"Text3"}),
            'TenNguoiDaiDien':forms.TextInput(attrs={'name':"TenNguoiDaiDien", 'type':"text", 'size':"60", 'maxlength':"200", 'id':"Text1"}),
            'TenTK':forms.TextInput(attrs={'name':"txtEmail", 'type':"text", 'size':"60", 'maxlength':"80", 'id':"Text2"}),
            'DienThoaiNguoiDaiDien':forms.TextInput(attrs={'name':"DienThoaiNguoiDaiDien", 'type':"text", 'size':"15", 'maxlength':"15", 'id':"Text11"}),
            'matinhthanh':forms.Select(attrs={'id':"soflow-color", 'width':"250", 'name':"matinhthanh", 'onchange':"showQuanhuyen(this.value)"},choices=tinhthanh_choices),
        }

