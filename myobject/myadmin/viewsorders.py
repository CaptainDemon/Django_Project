from django.http import HttpResponse
from django.shortcuts import redirect

from django.shortcuts import render
from myadmin.models import Orders
from myadmin.models import Goods
from myadmin.models import Details

# ===============订单信息管理======================
# 
# 查看订单
def  orders(request):
	list = Orders.objects.all()
	context = {"orderslist":list}
	return render(request,'myadmin/order/order.html',context)

# 订单详情
# detail: 订单id号 商品id号 商品名称 图片 单价 数量 
# 
# order: 会员id  联系人 地址 邮编 电话 购买时间 总金额 状态
# goods: 

def details(request):
	list =Details.objects.all() #
	for ob in list: #(orderid=ob.id)
		go = Goods.objects.get(id=ob.goodsid)

		de = Orders.objects.get(id=ob.orderid) #获取类别表(type)中id=商品表(goods)中的typeid的商品
		# 对象添加属性
		# ob.picname = ty.picname #商品图片
		# ob.goods = de.goodsid #商品价格   id 订单id号 商品id号 商品名称 单价数量
		
		ob.uid = de.uid
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

	# list = Details.objects.all()
	# for ob in list:
		# go = Goods.objects.get(id=ob.goodsid)




	context = {'detailslist':list}
	# print(list)
	# print(context)
	return render(request,"myadmin/order/details.html",context)