from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from quotes_app.models import Quote
from quotes_app.serializers import QuoteSerializer


@csrf_exempt
def quote_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    import pdb; pdb.set_trace()
    if request.method == 'GET':
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def quote_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        quote = Quote.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuoteSerializer(quote)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuoteSerializer(quote, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        quote.delete()
        return HttpResponse(status=204)