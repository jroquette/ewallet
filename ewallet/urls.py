"""ewallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from ewallet.documentation import schema_view
from apps.category.urls import category_urls
from apps.asset.urls import asset_urls
from apps.wallet.urls import wallet_urls
from apps.order.urls import order_urls
from apps.account.urls import account_urls

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/account/', include(account_urls)),
    path('api/asset/', include(asset_urls)),
    path('api/category/', include(category_urls)),
    path('api/order/', include(order_urls)),
    path('api/wallet/', include(wallet_urls)),
    path('api/get_token/', obtain_auth_token),
    path('api/auth/', include('rest_framework_social_oauth2.urls')),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
