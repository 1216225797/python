from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as vv

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # 不带参数的路由
    url(r'^test/',vv.funcA),
    # 带参数的路由
    # ？P代表传的参数
    url(r'^date/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',vv.funcB),

    # 反向解析
    url(r'^xiaoguo/',vv.rev,name='name')
]
