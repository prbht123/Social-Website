from django.http import HttpResponseBadRequest

def ajax_required(f):
    def wrap(request, *args, **kwargs):
        print(request)
        if not request.is_ajax():
            print("00000")
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    print("8888888888888888")
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap