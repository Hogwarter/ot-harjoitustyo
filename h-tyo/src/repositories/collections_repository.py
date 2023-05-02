from entities.collectabble import Collections
from repositories.users_repository import users_repository

class CollectionsRepository:
    def __init__(self, connection):
        self._connection = connection # Connection to collection
       
       
        