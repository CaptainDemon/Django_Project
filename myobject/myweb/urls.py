
from django.conf.urls import url

from . import views

urlpatterns = [
# 前台首页
	url(r'^$',views.index,name="myweb_index"),


# 列表页
	url(r'^list$',views.list,name ="myweb_list"),
#详情页
	url(r'^detail(?P<gid>[0-9]+)$',views.detail,name="myweb_detail"),


	
	#============================会员登录========================================
	# 用户登录
	url(r'^login$',views.login,name ="myweb_login"),
	url(r'^dologin$',views.dologin,name="myweb_dologin"),
	url(r'^logout$',views.logout,name="myweb_logout"),

	# 用户注册添加
	url(r'^register$',views.register,name ="myweb_register"),
	# 执行用户添加
	url(r'^doregister$',views.doregister,name ="myweb_doregister"),

	url(r'^order$',views.order,name ="myweb_order"),

	url(r'^member$',views.member,name ="myweb_member"),
	
	url(r'^myorder$',views.myorder,name ="myweb_myorder"),
# 购物车
	url(r'^cart$',views.cart,name ="myweb_cart"),
	url(r'^cartadd(?P<sid>[0-9]+)$',views.cartadd,name ="myweb_cartadd"),
	url(r'^cartdel(?P<sid>[0-9]+)$',views.cartdel,name ="myweb_cartdel"),
	url(r'^cartclear$',views.cartclear,name ="myweb_cartclear"),
	url(r'^cartchange$',views.cartchange,name ="myweb_cartchange"),




# 结算页面
	url(r'^verify$',views.verify,name="myweb_verify"),
	url(r'^verifyagain$',views.verifyagain,name="myweb_verifyagain"),




	# url(r'^dologin$',views.dologin,name="myadmin_dologin"),
	# url(r'^logout$',views.logout,name="myadmin_logout"),
	# url(r'^verify$', views.verify, name="myadmin_verify"), #验证码
]

