from django.conf.urls import patterns, include, url
from django.http.response import HttpResponseRedirect

urlpatterns = patterns('',
    # Examples:
    url(r'^$', lambda x: HttpResponseRedirect('/upload/new/')),
    url(r'^upload/', include('core.urls')),
    # url(r'^blog/', include('blog.urls')),

)

import os
urlpatterns += patterns('',
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
)
