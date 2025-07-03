import json

from django.contrib.auth import login
from django.contrib.auth.models import UserManager,AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(UserManager):
    def create_user(self, phone, password, is_staff=False, is_superuser=False, **kwargs):
        user = self.model(
            phone = phone,
            password = password,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **kwargs
        )
        user.set_password(str(password))
        user.save()
        return user

    def create_superuser(self, phone, password, **kwargs):
        return self.create_user(
            phone=phone,
            password=password,
            is_staff=True,
            is_superuser=True,
            **kwargs
        )

    def get_user(self, pk=None):
        if pk:
            return self.model.objects.filter(user_type=1, id=pk).first()
        else:
            return self.model.objects.filter(user_type=1)

    def get_admin(self,pk=None):
        if pk:
            return self.model.objects.filter(user_type=2, id=pk).first()
        else:
            return self.model.objects.filter(user_type=2)

class User(AbstractUser):
        # include
        ful_name = models.CharField(verbose_name=_('Isim Sharif'), max_length=128, null=True, blank=True)
        email = models.EmailField(blank=True, unique=False, verbose_name=_('Email'))
        phone = models.CharField(max_length=15, primary_key=False, unique=True,verbose_name=_('Telefon raqam'))
        user_date = models.DateTimeField(auto_now_add=True, auto_now=False)
        last_change = models.DateTimeField(auto_now_add=False, auto_now=True)

        #extra
        user_type = models.SmallIntegerField(default=1, choices=[
            (1, 'user'),
            (2, 'admin')
        ])

        is_staff = models.BooleanField(default=False)
        is_active = models.BooleanField(default=True)
        is_superuser = models.BooleanField(default=False)




        #excludu
        username = False
        first_name = False
        last_name = False


        objects = CustomUserManager()
        USERNAME_FIELD = 'phone'
        REQUIRED_FIELDS = ['user_type']

        def calculater_cart(self):
            carts = self.user_cart.filter(status=True)
            total_balance = 0
            valyuta = {
                "USD":12800,
                "RUB": 163,
                "UZS": 1
            }

            print("BU yedan sakrab o'tayabdi. sababi", carts, "pustoy")
            for i in carts:
                print("BU yerga kirmayabdi")
                cart_total = i.total_price
                price_type = i.product.price_type
                total_balance += cart_total * valyuta[price_type]

            print("\n\n", total_balance)
            return f"{ total_balance // 12800 }"

class OTP(models.Model):
    kalit = models.CharField('TOKEN', max_length=256, unique=True, primary_key=True)
    mobile = models.CharField(max_length=15)

    is_expired = models.BooleanField(default=False)
    tries = models.SmallIntegerField(default=0)
    extra = models.JSONField(default=json.dumps({}))
    is_verified = models.BooleanField(default=False)
    step = models.CharField(max_length=56, choices=[
        ('regis','Registration'),
        ('send', 'OTP send'),
        ('conf_regis', 'Registration'),

        ('login', 'Login'),
        ('send_login', 'OTP send'),
        ('conf_login' , 'Loggen in'),

    ])


    created = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def save(self,*args,**kwargs):
        if self.tries >= 3:
            self.is_expired=True
        if self.is_verified:
            self.is_expired = True
        return super(OTP ,self).save(*args,**kwargs)


    def check_expire_date(self):
        import datetime
        now = datetime.datetime.now()
        if (now-self.created).total_seconds() >=180:
            self.is_expired = True
            self.save()
            return False
        return True
