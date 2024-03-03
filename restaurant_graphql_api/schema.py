# core/schema.py

import graphene

import my_app.schema


class Query(my_app.schema.Query, graphene.ObjectType):
    # Combine the queries from different apps
    pass


class Mutation(my_app.schema.Mutation, graphene.ObjectType):
    # Combine the mutations from different apps
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)