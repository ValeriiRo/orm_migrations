from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    Student.objects.all().order_by(ordering)
    student = Student.objects.all()
    context = {'object_list': student}
    return render(request, template, context)
