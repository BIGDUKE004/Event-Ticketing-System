import unittest

from fastapi import HTTPException

from app.models.user import User
from app.services import auth_service


class AuthServiceTest(unittest.TestCase):

    def test_create_user(self):
        user = User.CreateUser(
            name= "miracle",
            email= "omogitbranchalmostwhyneme",
            password= "gitcollabisactuallyfun",
            role= "customer",
        )

        service = auth_service.AuthService()

        person : User.CreateUserRespone = service.create_user(user)
        self.assertEqual(service.get_count(), 1)
        self.assertEqual(person.name, "miracle")


    def test_user_creation(self):
        user = User.CreateUser(
            name= "miracle",
            email= "",
            password= "gitcollabisactuallyfun",
            role= "customer",
        )

        service = auth_service.AuthService()

        self.assertEqual(service.get_count(), 1)
        with self.assertRaises(HTTPException) as context:
            service.create_user(user)

