from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from django.shortcuts import redirect

from communicator_api.adapters.models.sql.short_url import ShortUrl
from communicator_api.serializers.short_url import ShortUrlSerializer, GetShortUrlSerializer
from communicator_api.tasks.worker.short_url import url_deactive, url_times_clicked


class ShortUrlViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):

    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer
    filterset_fields = ["type_url", "active", "expiration_date"]
    search_fields = ["long_url"]
    ordering = ["expiration_date"]

    def get_object_hash(self):
        return get_object_or_404(
            ShortUrl,
            hash_id=self.kwargs['pk']
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(GetShortUrlSerializer(data).data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object_hash()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['GET'])
    def deactivate(self, request, *args, **kwargs):
        instance = self.get_object_hash()
        instance.active = False
        instance.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def activate(self, request, *args, **kwargs):
        instance = self.get_object_hash()
        instance.active = True
        instance.save()
        return Response(status=status.HTTP_200_OK)

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
        return redirect(instance.long_url)
