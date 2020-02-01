from djongo import models
import datetime
# Create your models here.

class SMSHistory(models.Model):
    ThoiGian = models.DateField(default=datetime.date.today,null=True,blank=True)
    SoDienThoai = models.CharField(max_length=100,null=True,blank=True)
    SeriNo = models.CharField(max_length=100,null=True,blank=True)
    Count = models.IntegerField(default=0,null=True,blank=True)
class WebHistory(models.Model):
    ThoiGian = models.DateField(default=datetime.date.today,null=True,blank=True)
    DiaChiIP = models.CharField(max_length=100,null=True,blank=True)
    SoDienThoai = models.CharField(max_length=100,null=True,blank=True)
    SeriNo = models.CharField(max_length=100,null=True,blank=True)
    Count = models.IntegerField(default=0,null=True,blank=True)
class AppHistory(models.Model):
    ThoiGian = models.DateField(default=datetime.date.today,null=True,blank=True)
    DiaChiIP = models.CharField(max_length=100,null=True,blank=True)
    SoDienThoai = models.CharField(max_length=100,null=True,blank=True)
    SeriNo = models.CharField(max_length=100,null=True,blank=True)
    Count = models.IntegerField(default=0,null=True,blank=True)
class CallHistory(models.Model):
    ThoiGian = models.DateField(default=datetime.date.today,null=True,blank=True)
    SoDienThoai = models.CharField(max_length=100,null=True,blank=True)
    SeriNo = models.CharField(max_length=100,null=True,blank=True)
    Count = models.IntegerField(default=0,null=True,blank=True)
class History(models.Model):
    MaTem = models.CharField(max_length=100,null=True,blank=True)
    MaSP = models.CharField(max_length=100,null=True,blank=True)
    SMS = models.EmbeddedModelField(
        model_container = SMSHistory
    )
    App = models.EmbeddedModelField(
        model_container = AppHistory
    )
    Web = models.EmbeddedModelField(
        model_container = WebHistory
    )
    Call = models.EmbeddedModelField(
        model_container = CallHistory
    )


class sanpham(models.Model):
    MaSP = models.CharField(max_length=100)
    TenSP = models.CharField(max_length=100)
    NhaSX = models.CharField(max_length=100)
    LoaiSP = models.CharField(max_length=100)
    LoaiHang = models.IntegerField(default=0)
    NgayTao = models.DateField(default=datetime.date.today)
    LoaiHinhDN = models.CharField(max_length=100)
    MaCapPhep = models.CharField(max_length=100)
    GiayPhep = models.CharField(max_length=100)
    NgayCap = models.CharField(max_length=100)
    CapBoi = models.CharField(max_length=100)
    XuatXuSP = models.CharField(max_length=100)


class SPofDN(models.Model):
    MaDN = models.CharField(max_length=100)
    SanPham = models.EmbeddedModelField(
        model_container = sanpham
    )

class khotemact(models.Model):
    MaTem=models.CharField(max_length=30)
    MaDL=models.CharField(max_length=30)
    Serino=models.CharField(max_length=100)
    MaSP = models.CharField(max_length=100)
    NgayKichHoat=models.DateTimeField()
    SeriTem=models.CharField(max_length=100)

class thamso(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    value=models.IntegerField(default=0)


class imagefile(models.Model):
    anh=models.ImageField(upload_to='media/',null=True,blank=True)
    chuthich=models.TextField(default=' ')

class news(models.Model):
    title=models.TextField()
    ngaydang=models.DateField(auto_now_add=True)
    views=models.IntegerField(default=0)
    content=models.TextField()


