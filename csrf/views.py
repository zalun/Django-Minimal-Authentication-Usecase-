# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_POST


def main(request):
    return render_to_response('main.html',
            context_instance=RequestContext(request))

@require_POST
def register(request):
    if (request.POST.get('username', False)
            and request.POST.get('password', False)):
        User.objects.create_user(
                username=request.POST.get('username'),
                password=request.POST.get('password'),
                email='fake@example.com')
        return render_to_response('main.html', {'msg': 'User created'})
    return render_to_response('main.html', {'msg': 'User not created!'})

@login_required
@require_POST
def post(request):
    return render_to_response('main.html',
            {'msg': 'data received: "%s"' % request.POST.get('data', None)},
            context_instance=RequestContext(request))
