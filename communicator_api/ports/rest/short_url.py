from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from communicator_api.adapters.models.sql.short_url import ShortUrl
from communicator_api.serializers.short_url import ShortUrlSerializer, GetShortUrlSerializer


class ShortUrlViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):

    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(GetShortUrlSerializer(data).data, status=status.HTTP_201_CREATED)
