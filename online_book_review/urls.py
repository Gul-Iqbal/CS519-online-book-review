########### Import necessary Django modules ###########
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

########### Define URL patterns ###########
urlpatterns = [
    ########### Admin site URL ###########
    path('admin/', admin.site.urls),

    ########### Include URL patterns from the accounts app ###########
    path('', include('accounts.urls')),

    ########### Include URL patterns from the books app ###########
    path('books/', include('books.urls')),
]

########### Serve media files during development ###########
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
