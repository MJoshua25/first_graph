import graphene

# from graphene_django.types import DjangoObjectType

# from .models import *

# # Première essaie

# # class CategoryType(DjangoObjectType):
# #     class Meta:
# #         model = Category


# # class IngredientType(DjangoObjectType):
# #     class Meta:
# #         model = Ingredient


# # class Query(object):
# #     all_categories = graphene.List(CategoryType)
# #     all_ingredients = graphene.List(IngredientType)

# #     def resolve_all_categories(self, info, **kwargs):
# #         return Category.objects.all()

# #     def resolve_all_ingredients(self, info, **kwargs):
# #         # We can easily optimize query count in the resolve method
# #         return Ingredient.objects.select_related('category').all()

# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = Category


# class IngredientType(DjangoObjectType):
#     class Meta:
#         model = Ingredient


# class Query(object):
#     category = graphene.Field(CategoryType,
#                               id=graphene.Int(),
#                               name=graphene.String())
#     all_categories = graphene.List(CategoryType)


#     ingredient = graphene.Field(IngredientType,
#                                 id=graphene.Int(),
#                                 name=graphene.String())
#     all_ingredients = graphene.List(IngredientType)

#     def resolve_all_categories(self, info, **kwargs):
#         return Category.objects.all()

#     def resolve_all_ingredients(self, info, **kwargs):
#         return Ingredient.objects.all()

#     def resolve_category(self, info, **kwargs):
#         id = kwargs.get('id')
#         name = kwargs.get('name')

#         if id is not None:
#             return Category.objects.get(pk=id)

#         if name is not None:
#             return Category.objects.get(name=name)

#         return None

#     def resolve_ingredient(self, info, **kwargs):
#         id = kwargs.get('id')
#         name = kwargs.get('name')

#         if id is not None:
#             return Ingredient.objects.get(pk=id)

#         if name is not None:
#             return Ingredient.objects.get(name=name)

#         return None

from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import *

# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (relay.Node, )


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)