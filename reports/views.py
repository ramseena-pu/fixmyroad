from django.shortcuts import render
from rest_framework.views import APIView
from reports.models import RoadIssue
from reports.serializers import RoadIssueSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.
class RoadIssueListCreateView(APIView):
    def get(self,request):
        instance=RoadIssue.objects.all()
        serializer_instance=RoadIssueSerializer(instance,many=True)
        return Response(serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=RoadIssueSerializer(data=form_data)
        if serializer_instance.is_valid():
            instance=RoadIssue.objects.create(**form_data)
            serializer_instance=RoadIssueSerializer(instance)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class RoadIssueRetrieveUpdataDeleteView(APIView):
    def get(self,request,pk=None):
        instance=get_object_or_404(RoadIssue,id=pk)
        serializer_instance=RoadIssueSerializer(instance)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,pk=None):
        instance=get_object_or_404(RoadIssue,id=pk)
        form_data=request.data
        serializer_instance=RoadIssueSerializer(data=form_data)
        if serializer_instance.is_valid():
            RoadIssue.objects.filter(id=pk).update(**form_data)
            return Response(form_data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk=None):
        instance=get_object_or_404(RoadIssue,id=pk)
        instance.delete()
        return Response({"message":"Deleted"},status=status.HTTP_200_OK)


