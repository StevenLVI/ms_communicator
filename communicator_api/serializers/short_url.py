from communicator_api.adapters.models.sql.short_url import ShortUrl
from rest_framework import serializers
from config import SETUP
from hashids import Hashids


class GetShortUrlSerializer(serializers.Serializer):
    short_url = serializers.CharField()


class GetSUrlSerializer(serializers.Serializer):
    long_url = serializers.CharField()


class ShortUrlSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(default=True, required=False)

    class Meta:
        model = ShortUrl
        exclude = []

    def __create_hash__(self) -> object:
        return Hashids(salt=SETUP.HASH_IDS_SALT, min_length=SETUP.HASH_MIN_SIZE)

    def __generate_short_url__(self, hash_id: str) -> str:
        return f'{SETUP.HASH_DOMAIN}/{hash_id}'

    def __update_url__(self, id: int) -> object:
        hash_id = self.__create_hash__().encode(id)
        short_url = self.__generate_short_url__(hash_id)
        ShortUrl.objects.filter(id=id).update(hash_id=hash_id, short_url=short_url)
        return short_url

    def create(self, data):
        instanse = super().create(data)
        return {"short_url": self.__update_url__(instanse.id)}
