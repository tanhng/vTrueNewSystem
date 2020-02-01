from djongo import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
# from .managers import UserManager
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, TenTK, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not TenTK:
            raise ValueError('The given email must be set')
        TenTK = self.normalize_email(TenTK)
        user = self.model(TenTK=TenTK, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, TenTK, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(TenTK, password, **extra_fields)

    def create_superuser(self, TenTK, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(TenTK, password, **extra_fields)
    



class vtrueUser(AbstractBaseUser):
    # MADN=models.CharField(max_length=50, primary_key=True)
    # _id=models.CharField(max_length=100,null=True,blank=True)
    MaDN=models.CharField(max_length=100,null=True,blank=True)
    TenDN=models.CharField(max_length=100,null=True,blank=True)
    ngaydangky=models.DateField(auto_now_add=True,null=True,blank=True)
    DiaChiDangkyKD=models.CharField(max_length=200,null=True,blank=True)
    DienThoaiDN=models.CharField(max_length=15,null=True,blank=True)
    Fax=models.CharField(max_length=20,null=True,blank=True)
    NganhNgheKDChinh=models.CharField(max_length=255,null=True,blank=True)
    ThoigiandangkyKD=models.CharField(max_length=100,null=True,blank=True)
    DaiDienCMND=models.CharField(max_length=20,null=True,blank=True)
    TenNguoiDaiDien=models.CharField(max_length=50,null=True,blank=True)
    ChucDanh=models.CharField(max_length=128,null=True,blank=True)
    EmailNguoiDaiDien=models.EmailField(max_length=128,null=True,blank=True)
    DienThoaiNguoiDaiDien=models.CharField(max_length=20,null=True,blank=True)
    TenHoSoDinhKem=models.CharField(max_length=150,null=True,blank=True)
    TrangThaiDuyet=models.IntegerField(null=True,blank=True)
    NoiCapCMND=models.CharField(max_length=100,blank=True,null=True)
    NgayCapCMND=models.DateField(blank=True,null=True)
    DiaChiGiaoDich=models.CharField(max_length=200,blank=True,null=True)
    requeststatus=models.IntegerField(blank=True,null=True)
    matinhthanh=models.CharField(max_length=100,blank=True,null=True)
    quanhuyen=models.CharField(max_length=200,blank=True,null=True)
    TenTK=models.EmailField(max_length=128,unique=True,primary_key=True)
    is_staff=models.BooleanField(default=False,null=True,blank=True)
    is_active=models.BooleanField(default=False,null=True,blank=True)
    MaCapBac=models.IntegerField(null=True,blank=True)
    ThoiGian=models.DateTimeField(null=True,blank=True)
    SessionTime=models.CharField(max_length=255,null=True,blank=True)
    usertype=models.CharField(max_length=255,null=True,blank=True)
    tensohuu=models.CharField(max_length=200,null=True,blank=True)
    congty_phongban=models.CharField(max_length=200,null=True,blank=True)
    firstLogin=models.DateTimeField(null=True,blank=True)
    is_superuser=models.BooleanField(default=False,null=True,blank=True)
    objects = UserManager()
    USERNAME_FIELD = 'TenTK'
    REQUIRED_FIELDS = ['TenDN','DiaChiDangkyKD','matinhthanh','TenNguoiDaiDien','DienThoaiNguoiDaiDien','is_staff','is_active']

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser



# Create your models here.


# Create your models here.

