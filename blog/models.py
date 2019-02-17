# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.TextField(max_length=64, default='Title')
    content = models.TextField(null=True)
    pub_date = models.DateTimeField(null=True)
    def __unicode__(self):
        return self.title
