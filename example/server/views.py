from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

import opentracing

# Create your views here.

def server_index(request):
    return HttpResponse("Hello, world. You're at the server index.")

def server_simple(request):
    return HttpResponse("This is a simple traced request.")

def server_log(request):
    span = settings.OPENTRACING_TRACER.get_span(request)
    if span is not None:
        span.log_event("Hello, world!")
    return HttpResponse("Something was logged")

def server_child_span(request):
    span = settings.OPENTRACING_TRACER.get_span(request)
    if span is not None:
        child_span = settings.OPENTRACING_TRACER._tracer.start_span("child span", child_of=span.context)
        child_span.finish()
    return HttpResponse("A child span was created")
