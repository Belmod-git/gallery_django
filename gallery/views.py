from django.shortcuts import render,redirect
from .models import *

# Create your views here.

# 首页
def index(request):
    all_p = Painting.objects.all()
    return render(request,'index.html',{'index':all_p})

# 登录
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User(request,username=username,password=password)
        if user is None:
            return render(request,'login.html',{'error':"用户名密码错误"})
        else:
            return redirect('index')
    else:
        return render(request,'login.html')

# 添加
def add(request):
    if request.method == 'GET':
        return render(request,'add.html')
    else:
        name = request.POST.get('name')
        money = request.POST.get('money')
        image = request.POST.get('image')
        brief = request.POST.get('brief')
        info = request.POST.get('info')

        if not name or not money or not image or not brief or not info:
            return request(request,'error.html')

        a = Painting.objects.create(name=name,money=money,image=image,brief=brief,info=info)
        a.save()
        return redirect('index')


# 详情
def showinfo(request,aid):
    one = Painting.objects.get(id=aid)
    return render(request,'detail.html',{'one':one})


# 删除
def delete(request,aid):
    d = Painting.objects.get(id=aid)
    d.delete()
    return redirect('index')


# 修改
