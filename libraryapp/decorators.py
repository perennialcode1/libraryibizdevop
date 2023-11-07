from functools import wraps
from django.shortcuts import redirect

def session_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        username = request.session.get('email')
        if username is not None:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('sign_in') 
    return _wrapped_view
