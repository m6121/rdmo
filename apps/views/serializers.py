from django.template import Template, TemplateSyntaxError, Context

from rest_framework import serializers
from rest_framework import exceptions

from .models import View


class ViewIndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = View
        fields = (
            'id',
            'key',
            'comment',
            'title',
            'help'
        )


class ViewSerializer(serializers.ModelSerializer):

    def validate(self, data):
        # try to render the tamplate to see that the syntax is ok
        try:
            Template(data['template']).render(Context({}))
        except TemplateSyntaxError as e:
            raise exceptions.ValidationError({'template': [e.message]})

        return super(ViewSerializer, self).validate(data)

    class Meta:
        model = View
        fields = (
            'id',
            'uri_prefix',
            'key',
            'comment',
            'title_en',
            'title_de',
            'help_en',
            'help_de',
            'template'
        )


class ExportSerializer(serializers.ModelSerializer):

    class Meta:
        model = View
        fields = (
            'uri',
            'comment',
            'title_en',
            'title_de',
            'help_en',
            'help_de',
            'template'
        )
