from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404

from communicator_api.adapters.models.sql.short_url import ShortUrl
from communicator_api.serializers.short_url import ShortUrlSerializer, GetShortUrlSerializer, GetSUrlSerializer
from communicator_api.tasks.worker.short_url import url_deactive, url_times_clicked

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

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()

    @action(detail=True, methods=['GET'])
    def redirect(self, request, *args, **kwargs):
        instance = get_object_or_404(
            ShortUrl,
            hash_id=self.kwargs['pk'],
            active=True
        )
        if instance.type_url == "GENERIC":
            url_times_clicked.delay(instance.id)
        elif instance.type_url == "UNIQUE":
            url_deactive.delay(instance.id)
        return Response(GetSUrlSerializer(instance).data)
