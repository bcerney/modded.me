from rest_framework import generics

from quotes_app.models import Quote
from quotes_app.serializers import QuoteSerializer


class QuoteList(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


# @api_view(['GET', 'POST'])
# def quote_list(request, format=None):
#     """
#     List all quotes, or create a new quote.
#     """
#     if request.method == 'GET':
#         quotes = Quote.objects.all()
#         serializer = QuoteSerializer(quotes, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = QuoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def quote_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a quote.
#     """
#     try:
#         quote = Quote.objects.get(pk=pk)
#     except Quote.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = QuoteSerializer(quote)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = QuoteSerializer(quote, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         quote.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
