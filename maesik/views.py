from pydoc import doc
from xml.dom.minidom import Document
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from maesik.models import Document

# Create your views here.
# def calc(request):
#     return JsonResponse({'message': '테스트 성공!'})

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        file_obj = request.FILES['file']
        document = Document.objects.create(uploadedFile=file_obj)
        file_url = document.uploadedFile.url
        file_name = document.uploadedFile.name
        return Response({
            "file_name": file_name,
            "file_url": file_url
        })