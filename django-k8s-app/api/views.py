from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health(request):
    return Response({'status': 'healthy: v2'})


@api_view(['GET'])
def name(request):
    return Response({'name': 'name: v2'})
