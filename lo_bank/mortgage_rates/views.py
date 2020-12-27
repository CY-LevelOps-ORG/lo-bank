import logging
import tempfile
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

logger = logging.getLogger(__name__)

# Create your views here.

# CWE-601 URL Redirection to Untrusted Site ('Open Redirect')
def move(request):
    url = request.GET.get("next", "/")
    return HttpResponseRedirect(url)


def create_temp_file(request):
    filename = tempfile.mktemp()
    logger.info('Created temporary file %s', filename)
    return HttpResponse(status=200)