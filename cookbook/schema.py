import graphene
from cookbook.schema_mutations import Mutation
from cookbook.schema_queries import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
