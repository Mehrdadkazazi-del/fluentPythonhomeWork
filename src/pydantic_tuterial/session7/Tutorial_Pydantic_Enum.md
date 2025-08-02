
# Understanding the Python Code with Pydantic, Enum, and Type Validation

This document explains a Python code that demonstrates the use of **Pydantic**, **Enum**, **UUID**, and **Type Validation** in Python. It validates and structures data for a `Tshirt` model using `Pydantic` and Python's built-in `Enum` and `UUID`.

## Code Walkthrough

### 1. **Enum Class for Size**
```python
from enum import Enum

class Size(Enum):
    small = "small"
    medium = "medium"
    large = "large"
```

- **Enum** is a built-in class in Python used to create a set of constant values that can be used to represent different states or types. Here, we define a `Size` Enum with three possible values: `small`, `medium`, and `large`.
  
- **Why use Enum?**  
  Enums help organize sets of related constants (such as sizes), making the code more readable and less error-prone by avoiding hardcoding of string values.

### 2. **Pydantic Model for Tshirt**
```python
from pydantic import BaseModel, constr, conint
from typing_extensions import Optional
from uuid import UUID, uuid4

class Tshirt(BaseModel):
    brand: constr(min_length=2, strict=True, strip_whitespace=True, max_length=50)
    size: Size = Size.medium
    quantity: Optional[conint(ge=1, strict=True)] = 1
    id: UUID
    price: conint(ge=1, strict=True)
```

- **`BaseModel`**:  
  This is the base class in `Pydantic` that allows you to define models and automatically validate the data passed to them. This provides features like automatic data validation, parsing, and type checking.

- **`brand: constr(...)`**:  
  This is a constrained string (`constr`) with a minimum length of 2 characters, a maximum length of 50 characters, and automatic whitespace stripping. The `strict=True` option ensures that only strings are accepted (i.e., no non-string values like integers or floats).

- **`size: Size = Size.medium`**:  
  This field is of type `Size` which is our custom enum. The default value is `Size.medium`.

- **`quantity: Optional[conint(ge=1, strict=True)] = 1`**:  
  This field validates that the `quantity` is an integer greater than or equal to `1` (specified by `ge=1`). It is optional, with a default value of `1`. The `strict=True` flag ensures only integers are allowed (not floats).

- **`id: UUID`**:  
  This field expects a **UUID** (Universal Unique Identifier). The `UUID` type is used to ensure that the value conforms to the standard UUID format.

- **`price: conint(ge=1, strict=True)`**:  
  This is a constrained integer (`conint`) field for the price, ensuring that the value is an integer greater than or equal to `1`.

### 3. **Creating Instances of Tshirt**
```python
# this is get error because we input 1 character
t1 = Tshirt(brand = "k", size=Size.small, quantity=3, id=uuid4(), price=10)

t1 = Tshirt(brand = "kappa", size=Size.small, quantity=3, id=uuid4(), price=10)
print(t1)
```

- The first attempt to create a `Tshirt` object will raise a validation error because the `brand` field is constrained to be a string with a minimum length of 2 characters. You passed `"k"`, which is only one character, hence violating the validation constraint.
  
  **Expected Error**:
  ```
  pydantic.error_wrappers.ValidationError: 1 validation error for Tshirt
  brand
    ensure this value has at least 2 characters (type=value_error.any_str.min_length; limit_value=2)
  ```

- The second attempt creates a `Tshirt` object with a valid `brand` ("kappa"), which passes the validation.

### 4. **Output of Valid Object**
After creating a valid `Tshirt` object, we print the object:
```python
Tshirt(brand='kappa', size=<Size.small: 'small'>, quantity=3, id=UUID('f5d4a20a-e1b2-4c56-9901-3e4e56e68f25'), price=10)
```

- The printed output shows that the `Tshirt` object contains the correct attributes, including the `brand`, `size`, `quantity`, `id`, and `price`.

### Key Concepts Explained

- **Pydantic Validation**:  
  Pydantic automatically validates the data passed to the model. For instance, if the `brand` does not meet the minimum length constraint, it will raise an error.
  
- **Constrained Types**:  
  The use of `constr` and `conint` allows you to create constraints on the types of data that can be assigned to fields. For example, `constr(min_length=2)` ensures that the string is at least two characters long.

- **UUIDs**:  
  The `UUID` type ensures that the ID field follows the proper UUID format. This is especially useful when generating unique identifiers for records in a database or application.

- **Enums**:  
  Enums allow you to define a fixed set of values for a field. In this case, the `size` field can only be one of the values defined in the `Size` enum (small, medium, large).

### How to Run This Code

1. Install the necessary dependencies:
    ```bash
    pip install pydantic
    ```

2. Save the Python code in a `.py` file (e.g., `tshirt.py`).

3. Run the file using Python:
    ```bash
    python tshirt.py
    ```

4. The output will show the validation results and the creation of a valid `Tshirt` object.

---

## Conclusion

This code demonstrates the power of `Pydantic` for validating and parsing data in Python. By using `Enum`, `UUID`, and constrained types like `constr` and `conint`, we can enforce strict validation rules on the fields of our models. This is useful in scenarios where data integrity and consistency are important, such as when interacting with databases or APIs.

---

End of Document
