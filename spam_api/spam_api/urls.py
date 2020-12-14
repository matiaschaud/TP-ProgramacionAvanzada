"""spam_api URL Configuration

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


from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin
from mail_processed import views as mail_processed_views
from django.conf.urls import url

from rest_framework import routers
from rest_fwork import views as fwork_views
from rest_framework.authtoken import views as views_authtoken



from rest_framework.views import APIView
from rest_framework.response import Response
class test_if_logged(APIView):
    def get(self, request):
        return Response({'status':'ok!'})




from rest_fwork.views import EmailsDetail, EmailsList, QuotaInfo, EmailsListUser, EmailsDashboard, UsersDashboard, Login, Logout
from rest_framework import renderers


# email_detail = EmailsPredictedViewSet.as_view({
#     'get': 'retrieve',
# })

router = routers.DefaultRouter()
# router.register(r'users', fwork_views.UserViewSet)
# router.register(r'groups', fwork_views.GroupViewSet)
# router.register(r'emails', fwork_views.EmailsList)
# router.register(r'emails', email_list.viewset)


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # pag ppal
    path('', include(router.urls)),
    
    # servicios
    path('quota_info/',QuotaInfo.as_view()),
    path('process_email/', EmailsList.as_view(), name='emails-list'),
    path('process_email/<int:pk>/', EmailsDetail.as_view(), name='emails-detail'),
    path('history/<int:pk>/', EmailsListUser.as_view(), name='emails-list-user'),

    # Dashboard
    path('emails_dashboard/',EmailsDashboard.as_view()),
    path('users_dashboard/',UsersDashboard.as_view()),

    # token
    path('api-token-auth/', views_authtoken.obtain_auth_token),
    path('login/', Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view()),
]

