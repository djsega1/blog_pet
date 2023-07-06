from rest_framework.response import Response
from rest_framework.views import APIView

from homepage.models import Post
from homepage.serializers import PostSerializer


class GetAllPostView(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer.data)
