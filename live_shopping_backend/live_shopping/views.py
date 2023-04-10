from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from live_shopping.dyte_api_client import DyteAPIClient
from live_shopping.models import LiveVideoRequest
from live_shopping.serializers import LiveVideoRequestSerializer

class LiveVideoRequestViewSet(ViewSet):
	pass