from marshmallow import validate as validate
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema, Relationship

from app.api.helpers.utilities import dasherize


class FaqSchema(Schema):
    """
    Api schema for page Model
    """
    class Meta:
        """
        Meta class for page Api Schema
        """
        type_ = 'faq'
        self_view = 'v1.faq_detail'
        self_view_kwargs = {'id': '<id>'}
        inflect = dasherize

    id = fields.Str(dump_only=True)
    question = fields.Str(required=True)
    answer = fields.Str(required=True)
    event = Relationship(attribute='event',
                         self_view='v1.faq_event',
                         self_view_kwargs={'id': '<id>'},
                         related_view='v1.event_detail',
                         related_view_kwargs={'faq_id': '<id>'},
                         schema='EventSchemaPublic',
                         type_='event')