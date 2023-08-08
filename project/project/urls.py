"""
Our project URL Configuration

The `url_patterns` list is responsible for routing URLs to appropriate views.

"""

from django.contrib import admin
from django.urls import path, include

url_patterns = [
    path('admin/', admin.site.urls),
    path('web_pages/', include('django.contrib.flatpages.urls')),
]
