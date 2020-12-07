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



from rest_framework.views import APIView
from rest_framework.response import Response
class test_if_logged(APIView):
    def get(self, request):
        return Response({'status':'ok!'})




from rest_fwork.views import EmailsDetail, EmailsList, UserList, UserDetail, Login, Logout
from rest_framework import renderers
from rest_framework.authtoken import views as views_authtoken

from rest_framework_jwt.views import verify_jwt_token
from rest_framework_jwt.views import refresh_jwt_token


# email_detail = EmailsPredictedViewSet.as_view({
#     'get': 'retrieve',
# })

router = routers.DefaultRouter()
# router.register(r'users', fwork_views.UserViewSet)
# router.register(r'groups', fwork_views.GroupViewSet)
# router.register(r'emails', fwork_views.EmailsList)
# router.register(r'emails', email_list.viewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba',mail_processed_views.probando_emails),

    # REST API
    path('', include(router.urls)),
    path('process_email/', EmailsList.as_view(), name='emails-list'),
    path('process_email/<int:pk>/', EmailsDetail.as_view(), name='emails-detail'),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('test_if_logged',test_if_logged.as_view()),
    # rest api token
    path('api-generate-token/', views_authtoken.obtain_auth_token),
    path('login/', Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view()),

    # # TOKEN
    # path('api-token-auth/', obtain_jwt_token),
    # path('api-token-refresh/', refresh_jwt_token),
    # path('api-token-verify/', verify_jwt_token),

    
]

