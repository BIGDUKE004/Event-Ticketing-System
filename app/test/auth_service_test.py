import unittest

from fastapi import HTTPException

from app.models.user import User
from app.services import auth_service
from repositories.in_memory_user_repository import InMemoryUserRepository


class AuthServiceTest(unittest.TestCase):

    def test_create_user(self):
        user = User.CreateUser(
            name= "miracle",
            email= "omogitbranchalmostwhyneme",
            password= "gitcollabisactuallyfun",
            role= "customer",
        )

        service = auth_service.AuthService(InMemoryUserRepository())

        person : User.CreateUserRespone = service.create_user(user)
        self.assertEqual(service.get_count(), 1)
        self.assertEqual(person.name, "miracle")


    def test_user_create_account_with_one_missing_feilds(self):
        user = User.CreateUser(
            name= "miracle",
            email= "",
            password= "gitcollabisactuallyfun",
            role= "customer",
        )

        service = auth_service.AuthService(InMemoryUserRepository())

        self.assertEqual(service.get_count(), 0)
        with self.assertRaises(HTTPException) as context:
            service.create_user(user)

    def test_user_create_account_with_two_missing_feilds(self):
        user = User.CreateUser(
            name="miracle",
            email="",
            password="",
            role="customer",
        )

        service = auth_service.AuthService(InMemoryUserRepository())

        self.assertEqual(service.get_count(), 0)
        with self.assertRaises(HTTPException) as context:
            service.create_user(user)


    def test_user_logsin_after_creating_account(self):
        user = User.CreateUser(
            name="miracle",
            email= "omogitbranchalmostwhyneme",
            password= "gitcollabisactuallyfun",
            role="customer",
        )

        service = auth_service.AuthService(InMemoryUserRepository())
        person : User.CreateUserRespone = service.create_user(user)
        self.assertEqual(service.get_count(), 1)
        self.assertEqual(person.name, "miracle")

        user = User.LoginUser(
            email= "omogitbranchalmostwhyneme",
            password= "gitcollabisactuallyfun",
        )

        login_response : User.LoginRespone = service.login_user(user)
        self.assertEqual("login successful", login_response.message)


    def test_user_logsin_with_one_missing_field_after_creating_account(self):
        user = User.CreateUser(
            name="miracle",
            email= "omogitbranchalmostwhyneme",
            password= "gitcollabisactuallyfun",
            role="customer",
        )

        service = auth_service.AuthService(InMemoryUserRepository())
        person : User.CreateUserRespone = service.create_user(user)
        self.assertEqual(service.get_count(), 1)
        self.assertEqual(person.name, "miracle")

        user = User.LoginUser(
            email= "",
            password= "gitcollabisactuallyfun",
        )
        with self.assertRaises(HTTPException) as context:
            service.login_user(user)
