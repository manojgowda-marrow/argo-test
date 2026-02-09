from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health(request):
    return Response({'status': 'healthy'})


@api_view(['GET'])
def name(request):
    return Response({'name': 'Django K8s App, second sync'})
