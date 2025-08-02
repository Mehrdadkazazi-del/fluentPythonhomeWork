from enum import Enum

from pydantic import BaseModel, constr, conint
from typing_extensions import Optional
from uuid import UUID,uuid4

class Size(Enum):
    small = "small"
    medium = "medium"
    large = "large"


class Tshirt(BaseModel):
    brand: constr(min_length=2, strict=True, strip_whitespace=True, max_length=50)
    size: Size = Size.medium
    # ge = 1 means (x>=1)
    quantity: Optional[conint(ge=1, strict=True)] = 1
    id: UUID
    price: conint(ge=1, strict=True)


# this is get error because we input 1 character
t1 = Tshirt(brand = "k", size=Size.small, quantity=3, id=uuid4(), price=10)

t1 = Tshirt(brand = "kappa", size=Size.small, quantity=3, id=uuid4(), price=10)
print(t1)