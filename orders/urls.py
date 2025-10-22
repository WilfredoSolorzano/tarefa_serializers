#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.urls import include, path
from rest_framework import routers

from orders import viewsets

router = routers.SimpleRouter()
router.register(r"orders", viewsets.OrderViewSet, basename="orders")


urlpatterns = [
    path("", include(router.urls)),
]
