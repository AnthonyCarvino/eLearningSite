
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Course, Step


def courseList(request):
    courses = Course.objects.all()
    return render(request,'courses/courseList.html', {'courses': courses})

def courseDetail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/courseDetail.html', {'course': course})

def stepDetail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id = course_pk, pk = step_pk)
    return render(request, 'courses/stepDetail.html', {'step': step})