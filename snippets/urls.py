from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'), # 5. Relationships & Hyperlinked
    url(r'^$', views.api_root), # 5. Relationships & Hyperlinked
    url(r'^users/$', views.UserList.as_view(), name='user-list'), # 4. Authentication and Permission
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'), # 3. class-based views
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    # url(r'^snippets/$', views.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)