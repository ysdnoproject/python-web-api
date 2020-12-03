from django.http import JsonResponse


def index(request):
    book_list = [
        {'id': 1, 'name': 'ptyhon'},
        {'id': 2, 'name': 'go'},
    ]
    return JsonResponse(book_list, safe=False)
