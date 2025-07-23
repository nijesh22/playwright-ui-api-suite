from dataclasses import dataclass
import random
import lorem

@dataclass
class UserData:
    name: str
    email: str
    password: str
    first_name: str
    last_name: str
    address: str
    state: str
    city: str
    zipcode: str
    mobile_no: str

def generate_user_data(password: str = None) -> UserData:
    return UserData(
        name="TestUser",
        email=f"nijeshplaywright{random.randint(1000,9999)}@test.com",
        password=  password or f"qwerty@{random.randint(1000,9999)}",
        first_name=f"nijesh{random.randint(100,999)}",
        last_name=f"playwright{random.randint(100,999)}",
        address=lorem.sentence(),
        state="ontario",
        city="toronto",
        zipcode="12345",
        mobile_no="1234567890"
    )
