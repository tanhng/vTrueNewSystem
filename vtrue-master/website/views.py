from django.shortcuts import render, redirect
from user.models import vtrueUser
from website.models import History, SPofDN, khotemact, SMSHistory, AppHistory, WebHistory, CallHistory,news as tintuc,imagefile
from django.contrib.auth import authenticate
from django.urls import reverse
import csv
from django.views import View
from django.http import HttpResponse
from .forms import CountForm
from djongo import models
from django.http import HttpResponse
import xlwt
# Create your views here.


def main(request):
    return render(request, 'website/main.html')


def intro(request):
    return render(request, 'website/intro.html')


def news(request):
    a=tintuc.objects.all()[0]
    print(a.content)
    print(a.content.split('@@@'))
    arr=a.content.split('@@@')
    mylist=[]
    for x in arr:
        print(x)
        print("media/{}".format(x))
        b=imagefile.objects.filter(anh='media/{}'.format(x))
        if len(b)>0:
            mylist.append({'check':'1','value':b[0].anh,'chuthich':b[0].chuthich})
            print('anh b',b[0].anh)
        else:
            mylist.append({'check':'0','value':x})
    print('my list',mylist)
    return render(request, 'website/news.html',{'cl':mylist})


def company(request):
    return render(request, 'website/company.html')


def feedback(request):
    return render(request, 'website/feedback.html')


def register(request):
    return render(request, 'website/register.html')


def sign_in(request):
    return render(request, 'website/sign-in.html')


class DSSP:
    def __init__(self, tenSP, count):
        self.tenSP = tenSP
        self.count = count


def count(request):
    if request.user.is_authenticated:
        user1 = vtrueUser.objects.get(TenTK=request.user)
        print('user ne', user1.MaDN)
        item = SPofDN.objects.filter(MaDN=user1.MaDN)

        list = []
        for sp in item:
            i = sp.SanPham
            k = i.MaSP
            toCount = History.objects.filter(MaSP=k)
            print(toCount)
            count = 0
            for x in toCount:
                print(x.SMS.Count)
                count = x.SMS.Count + x.Web.Count + x.Call.Count + x.App.Count

            list.append(DSSP(i.TenSP, count))

        return render(request, 'website/VTrue Service.html', {'username': request.user, 'count': list})

    else:
        return HttpResponse('sai')


class check(View):
    def get(self, request):
        return render(request, 'website/main.html')

    def post(self, request):
        matem = request.POST.get('txtCheck')
        print(matem)
        temp = khotemact.objects.filter(MaTem=matem)
        if len(temp)==0:
            return HttpResponse('Hàng Fake')
        else:
            print(temp[0])
            tim = History.objects.filter(MaTem=temp[0].MaTem)
            if len(tim) == 0:
                them = History.objects.create(MaTem=temp[0].MaTem, MaSP='123',
                    SMS=SMSHistory.objects.get_or_create(
                        ThoiGian='2010-1-1',
                        SoDienThoai='12324',
                        SeriNo='12343',
                        Count=0
                )[0],
                    App=AppHistory.objects.get_or_create(
                        ThoiGian='2010-1-1',
                        DiaChiIP='1',
                        SoDienThoai='12324',
                        SeriNo='12343',
                        Count=0
                )[0],
                    Web=WebHistory.objects.get_or_create(
                        ThoiGian='2010-1-1',
                        DiaChiIP='1',
                        SoDienThoai='12324',
                        SeriNo='12343',
                        Count=1
                )[0],
                    Call=CallHistory.objects.get_or_create(
                        ThoiGian='2010-1-1',
                        SoDienThoai='12324',
                        SeriNo='12343',
                        Count=0
                )[0]
                )

                them.save()
            else:
                History.objects.filter(MaTem=temp[0].MaTem).update(
                    Web={'Count': tim[0].Web.Count+1})
                if tim[0].SMS.Count + tim[0].Web.Count + tim[0].Call.Count + tim[0].App.Count > 4:
                    return HttpResponse('Cảnh báo')
                else:
                    return HttpResponse('oke')


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['so tt', 'ten san pham', 'luot tra cuu',  ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    # get list
    user1 = vtrueUser.objects.get(TenTK=request.user)
    print('user ne', user1.MaDN)
    item = SPofDN.objects.filter(MaDN=user1.MaDN)

    list = []
    for sp in item:
        i = sp.SanPham
        k = i.MaSP
        toCount = History.objects.filter(MaSP=k)
        print(toCount)
        count = 0
        for x in toCount:
            print(x.SMS.Count)
            count = x.SMS.Count + x.Web.Count + x.Call.Count + x.App.Count

        list.append(DSSP(i.TenSP, count))

    rows = list
    for row in rows:
        row_num += 1
        ws.write(row_num, 0, row_num, font_style)
        ws.write(row_num, 1, row.tenSP, font_style)
        ws.write(row_num, 2, row.count, font_style)


    wb.save(response)
    return response
