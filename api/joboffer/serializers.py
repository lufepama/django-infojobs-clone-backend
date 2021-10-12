from rest_framework import serializers


class JobOfferSerializer(serializers.BaseSerializer):

    def to_representation(self, instance):
        return {
            'titleOffer': instance.title,
            'publishDate': instance.publish_date,
            'companyInfo': instance.get_company_info,  # Name, location
            'lowerSalary': instance.lower_salary,
            'upperSalary': instance.upper_salary,
            'imagen': instance.get_company_imagen
        }
