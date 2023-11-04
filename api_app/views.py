from django.shortcuts import render
from .serailizers import UserRegistrationSerializer, StudentSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from mainapp.models import Student
from api_app.filters import StudentFilter
from rest_framework import viewsets  
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.db.models import F



class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class StudentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = StudentFilter
    pagination_class = PageNumberPagination
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(total_marks=(F('marks_hindi') + F('marks_english') + F('marks_math') + F('marks_science') + F('marks_grography')))
        queryset = queryset.order_by('-total_marks')

        return queryset

