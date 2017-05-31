from rest_framework.serializers import ModelSerializer, RelatedField, PrimaryKeyRelatedField, HyperlinkedModelSerializer
from products.models import Product

# class ChildSerializer(HyperlinkedModelSerializer):
#
#     parent_id = PrimaryKeyRelatedField(queryset=Parent.objects.all(),source='parent.id')
#     # parent_id = RelatedField(read_only=True)
#
#     class Meta:
#         model = Child
#         fields = ('child_name','parent_id')
#
#     def create(self, validated_data):
#         child = Child.objects.create(parent=validated_data['parent']['id'], child_name=validated_data['child_name'])
#
#         return child
#
#
# class ParentSerializer(HyperlinkedModelSerializer):
#     children = ChildSerializer(many=True, read_only=True)
#     class Meta:
#         model = Parent
#         fields = ('name','children')

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
