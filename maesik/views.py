from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def calc(request):
    return JsonResponse({'message': '테스트 성공!'})