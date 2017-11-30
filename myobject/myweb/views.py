from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
# Create your views here.
from myadmin.models import Types,Goods
from myadmin.models import Goods,Details
from myweb.models import Goods,Orders

from myadmin.models import Users
from django.shortcuts import redirect
from django.core.urlresolvers  import reverse
import time,json,os
from django.http import HttpResponseRedirect  #重定向映入
from myweb.models import webusers

# 公共信息加载函数
def loadinfo():
	context = {}
	context['type0list'] = Types.objects.filter(pid = 0)
	return context

# 前台首页
def index(request):
    # context = loadinfo()
    # list = Goods.objects.all()
    # context['goodslist']=list
    context = loadinfo()
    goodslist = Goods.objects.filter()
    if request.GET.get('tid','') != '':
        tid = str(request.GET.get('tid'))
        goodslist = goodslist.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+tid+','))
    context['goodslist'] = goodslist

    return render(request,'myweb/index.html',context)

    # # 列表页
    # def list(request):
    #     context = loadinfo()
    #     list = Goods.objects.filter()
    # 	# where = []
    #     if request.GET.get('tid') != '':
    #         tid = str(request.GET.get('tid',''))
    #         list= list.filter(typeid__in = Types.objects.only('id').filter(path__contains = ','+tid+','))
    # 	# ob = Goods.objects.get(id=7)
    #     context ['goodslist']=list
    # 	# context = {'goods':ob}
    # 	# print(context)

    #     return render(request,'myweb/list.html',context)

# 列表页
def list(request):
    context = loadinfo()
    goodslist = Goods.objects.filter()
    if request.GET.get('tid','') != '':
        tid = str(request.GET.get('tid'))
        goodslist = goodslist.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+tid+','))
    context['goodslist'] = goodslist

    return render(request,"myweb/list.html",context)

# 详情页
def detail(request,gid):
	context = loadinfo()

	ob = Goods.objects.get(id=gid)
	context["goods"]=ob
	return render(request,'myweb/detail.html',context)

# ==============前台会员操作====================
# 会员信息添加表单
def register(request):

    return render(request,'myweb/register.html')

#执行会员信息添加    
def doregister(request):
    try:
        ob = webusers()
        ob.username = request.POST['account']
        # ob.name = request.POST['name']
        #获取密码并md5
        import hashlib
        m = hashlib.md5() 
        m.update(bytes(request.POST['password'],encoding="utf8"))
        ob.password = m.hexdigest()


        ob.state = 1
        ob.addtime = time.time()
        ob.save()
        # context = {'info':'添加成功！'}
        return render(request,"myweb/login.html")

    except:
        return render(request,"myweb/register.html")

# 会员登录表单
def login(request):
    # print('=====login==')
    # if request.session['loginstate'] = 1:

    return render(request,'myweb/login.html')

# 会员执行登录
def dologin(request):
    # print('===dologin====')
    #     # 校验验证码
    # verifycode = request.session['verifycode']
    # code = request.POST['code']
    # if verifycode != code:
    #     context = {'info':'验证码错误！'}
    #     return render(request,"myweb/login.html",context)
    try:
        #根据账号获取登录者信息
        user = Users.objects.get(username=request.POST['account']) #accout=username
        #判断当前用户是否是前台启用用户
        if user.state == 1:
            # 验证密码
            import hashlib
            m = hashlib.md5() 
            m.update(bytes(request.POST['password'],encoding="utf8"))

            if user.password == m.hexdigest():
                # 此处登录成功，将当前登录信息放入到session中，并跳转页面
                # request.session['"adminuser"+user.id'] = user.name 
                # #????????????????????????????????是否可以让session值唯一
                
                request.session['adminuser'] = user.name
                request.session['loginstate'] = 1
                request.session['uid'] = user.id

                #print(json.dumps(user))
                return redirect(reverse('myweb_index'))
            else:
                context = {'info':'登录密码错误！'}

        else:
            context = {'info':'此用户非前台启用用户！'}
    except:
        context = {'info':'登录账号错误！'}
    return render(request,"myweb/login.html",context)

# 推出登录
def logout(request):
    request.session['loginstate'] = 0
    context = loadinfo()
    request.session['shoplist'] = {}


    # del request.session['adminuser']
    # return render(,'myweb/index.html')
    # 方法 
    # context = loadinfo()
    # return HttpResponse('欢迎进入商城网址qiian台!')
    # return render(request,'myweb/index.html',context)



    # 重定向,反向解析??????????????????????????????
    # return redirect(reverse('index'))  #参数--->views.index或者url别名 name= "myweb_index"
    #方法1 ('路径如:myweb/html')
         # return HttpResponseRedirect('/') #浏览器重定向
    # 不带带参数    
    #return HttpResponseRedirect('/commons/invoice_return/index/') #跳转到index界面  
    #带
    #return HttpResponseRedirect('/commons/invoice_return/index/?message=error') #跳转到index界面  
    # 方法2
        # return redirect(reverse('views.index')) #url里的views.index
    return redirect(reverse('myweb_index')) #url里的name

    # return redirect(reverse('commons.views.invoice_return_index', args=[])) #跳转到index界面

# 注册页
def register(request):

    return render(request,'myweb/register.html')

# 个人中心
def member(request):

    return render(request,'myweb/member.html')

# 购物车
def cart(request):
    # list = request.session['shoplist']
    # if 'shoplist' not in request.session:
        return render(request,'myweb/cart.html')
        # return render(request,'myweb/cart.html',context)


    # print(list)
    # for goods,g in list:
    #     list2 = Goods.objects.filter(id = g)
    # context = {'cartslist':list2}
    # return render(request,'myweb/cart.html',context)

# 加入购物车
def cartadd(request,sid):
    # 获取要放入购物车中的商品信息
    goods = Goods.objects.get(id=sid) 
    shop = goods.toDict();
    # print(shop,type(shop))


    shop['m'] = int(request.POST['m']) #添加一个购买量属性
    if 'shoplist' in request.session:
        
        shoplist = request.session['shoplist']

    else:
        shoplist = {}
    # 判断此商品是否在购物车中
    if sid in shoplist:
        shoplist[sid]['m']+=shop['m']
    else:
        # 新加商品
        shoplist[sid] = shop
    # 将购物车信息放回到session
    request.session['shoplist'] = shoplist
    return redirect(reverse('myweb_cart'))
    # return render(request,'myweb/cart.html')

    # m = request.POST['num']
    # i = request.POST['goods.id']
    # print(i)
    # print(m)

    # num = int(m)
    # context = loadinfo()
    # list = Goods.objects.filter(id=i)
    # print(num)
    # print(i)
    # context = {'goodslist':list}
    # return redirect(reverse('myweb_cart'),context) #url里的name

#删除
def cartdel(request,sid):
    shoplist = request.session['shoplist']
    del shoplist[sid]
    request.session['shoplist'] = shoplist
    return redirect (reverse('myweb_cart'))
     
# 清空购物车
def cartclear(request):
    context = loadinfo()
    request.session['shoplist'] = {}
    return render(request,"myweb/cart.html",context)

# 改变商品数量
def cartchange(request):
    context = loadinfo()
    shoplist = request.session['shoplist']
    # 获取信息
    shopid = request.GET['sid']
    num = int(request.GET['num'])
    if num<1:
        num = 1
    shoplist[shopid]['m'] =num 
    #改变商品数量
    request.session['shoplist'] = shoplist
    return render(request,"myweb/cart.html",context)

#确认信息
def verify(request):

    # details = Details.objects.filter(uid=request.session['uid']) #accout=username
    # request.session['linkman'] = details.linkman
    # request.session['phone'] = details.phone
    # request.session['address'] = details.address

    list =Details.objects.all() 
    for ob in list: #(orderid=ob.id)
        go = Goods.objects.get(id=ob.goodsid)
        de = Orders.objects.get(id=ob.orderid)
        ob.linkman = de.linkman
        ob.address = de.address
        ob.code = de.code
        ob.phone = de.phone
        ob.addtime = de.addtime
        ob.total = de.total
        ob.status = de.status
        ob.name = go.goods
        ob.price = go.price
        ob.total = ob.num * ob.price
    context = {'detailslist':list}
    return render(request,'myweb/verify.html',context)

    # return render(request,'myweb/verify.html')

def verifyagain(request):
    list =Details.objects.all() 
    for ob in list: #(orderid=ob.id)
        go = Goods.objects.get(id=ob.goodsid)
        de = Orders.objects.get(id=ob.orderid)
        # ob.linkman = de.linkman
        ob.linkman = request.POST['linkman']

        # ob.address = de.address
        ob.address = request.POST['address']

        ob.code = de.code
        ob.phone = de.phone
        ob.addtime = de.addtime
        ob.total = de.total
        ob.status = de.status
        ob.name = go.goods
        ob.price = go.price
        ob.total = ob.num * ob.price
    context = {'detailslist':list}
    return render(request,'myweb/verifyagain.html',context)

    # return render(request,'myweb/verify.html')
# order订单
def order(request):

    return render(request,'myweb/order.html')
# 我的订单
def myorder(request):

    return render(request,'myweb/myorder.html')
