import jsonschema
import django.core
from django.utils.translation import gettext_lazy as _


class JSONSchemaValidator:
    def __init__(self, schema):
        self.schema = schema

    def __call__(self, value):
        try:
            jsonschema.validate(value, self.schema)
        except jsonschema.exceptions.ValidationError:
            raise django.core.exceptions.ValidationError(
                _('%(value)s Esquema invalído'), params={'value': value}
            )
