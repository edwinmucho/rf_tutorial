#############################################################################################################
# 6. Veiwsets & Routers
#############################################################################################################
# from snippets.views import SnippetViewSet, UserViewSet, api_root  # Using Routers
# from rest_framework import renderers # Using Routers
# from rest_framework.urlpatterns import format_suffix_patterns # Using Routers
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter # Using Routers
from snippets import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns=[
    url(r'^', include(router.urls))
]

# If use router, it very simple
# snippet_list = SnippetViewSet.as_view({
#     'get' : 'list',
#     'post': 'create',
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get' : 'retrieve',
#     'put' : 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight',
# }, renderer_classes=[renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view({
#     'get' : 'list',
# })
# user_detail = UserViewSet.as_view({
#     'get' : 'retrieve',
# })
#
# urlpatterns = format_suffix_patterns([
#     url(r'^$', api_root),
#     url(r'^snippets/$', snippet_list, name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
# ])
#############################################################################################################

#############################################################################################################
# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views
#
# urlpatterns = [
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'), # 5. Relationships & Hyperlinked
#     url(r'^$', views.api_root), # 5. Relationships & Hyperlinked
#     url(r'^users/$', views.UserList.as_view(), name='user-list'), # 4. Authentication and Permission
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
#     url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'), # 3. class-based views
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
#     # url(r'^snippets/$', views.snippet_list),
#     # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
#############################################################################################################