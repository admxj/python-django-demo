# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'pub_date')
    list_filter = ('pub_date', )
    pass


admin.site.register(models.Article, ArticleAdmin)
