from rest_framework import serializers


class CompanySerializer(serializers.BaseSerializer):
    def to_representation(self, instance):

        return instance.get_company_info
