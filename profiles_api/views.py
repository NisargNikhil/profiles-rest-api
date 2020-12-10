from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of API features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a tradtional django view',
            'gives you the most control over the apps logic',
            'Is mapped manually to Urls',
        ]
        return Response({'message': 'Hello','an_apiview': an_apiview})
