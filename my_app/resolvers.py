# my_app/resolvers.py

import graphene
from graphql_jwt.decorators import login_required

class Query(graphene.ObjectType):
    @login_required
    def resolve_private_data(self, info):
        # Resolver logic for private data
        pass