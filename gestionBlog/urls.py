from django.conf.urls import include, url
import gestionBlog.views as views

urlpatterns = [
    url(r'^$', views.post_list, name="home"),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name':'admin/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name':'gestionBlog/see_you_soon.html'}),
    url(r'^accounts/profile/$', views.show_home_after_login_logout),
    url(r'^post/new/$', views.add_post, name="add_post"),
    url(r'^post/(?P<pk>[-\w]+)/$', views.post_detail),
    url(r'^post/(?P<pk>[-\w]+)/edit/$', views.edit_post, name="post_edit"),
    url(r'^post/(?P<pk>[-\w]+)/delete/$', views.delete_post, name="delete_post"),
    url(r'^comment/(?P<pk>[-\w]+)/$', views.add_comment_to_post, name="add_comment_to_post"),
    url(r'^comment/(?P<pk>[-\w]+)/remove/$', views.delete_comment_to_post, name="delete_comment_to_post"),
]
