from products.models import Products
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl import Document


@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'products'
        settings = {
            "number_of_shards": 1,
            "number_of_replicas":0
        }

    class Django:
        model = Products
        fields = [
            "id",
            "product_name",
            "brand",
            "price",
        ]