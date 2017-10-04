from django.conf.urls import url
from demo_app import views

app_name='demo_app'


urlpatterns=[
url(r'^$',views.index_page,name='index'),
url(r'^login/$',views.user_login, name='login'),
url(r'^register/$',views.register_page,name='register'),
url(r'^appointment/$',views.appointment,name='appointment'),
url(r'^create_appointment/$',views.create_appointment,name='create_appointment'),
url(r'^others_site/$',views.others_site,name='other_name')
]
