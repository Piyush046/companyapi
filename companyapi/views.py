from django.http import HttpResponse, JsonResponse


def home_page(request):

    dost=['piyush','rahul','ravi']
    return JsonResponse(dost, safe=False) 