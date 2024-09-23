from pydantic import BaseModel, parse_obj_as


class Geo(BaseModel):
    lat: str
    lng: str


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company


class UsersPars:
    @staticmethod
    def users_pars(users):
        users_pars = parse_obj_as(list[User], users)
        return users_pars
