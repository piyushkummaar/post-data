from django.http import HttpResponse

def home(request):
    # print(dir(request))
    # print(request.session)
    # return HttpResponse('<h1>Hello World!!</h1>')
    response = HttpResponse(content_type='application/json')
    
    response.content = 'hellkjDGK HJGSkj'
    response.status_code = 404
    return response