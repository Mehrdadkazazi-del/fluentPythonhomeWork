## Description

This code defines a **`Student`** class using **Pydantic**, a library for data validation and settings management in Python. The purpose of the class and code is to validate and transform data structures (such as JSON objects) into Python objects with strong typing, while supporting aliasing and snake_case fields for convenience.

---

### Key Features:

1. **Class Definition**:
   - The `Student` class inherits from `BaseModel` provided by Pydantic.
   - Fields include `first_name`, `last_name`, and `student_number`, which can accept data using aliases (`firstName`, `lastName`, `studentNumber`) commonly used in JSON.

2. **Field Aliases**:
   - The `Field` function defines aliases for attributes (e.g., `first_name` uses the alias `firstName`).
   - This is particularly useful when working with external APIs or systems using camelCase naming conventions.

3. **`populate_by_name` Config**:
   - The `Config` subclass sets `populate_by_name = True`, allowing input data to use either the aliases (`firstName`) or the actual Python attribute names (`first_name`).

4. **Validation and Transformation**:
   - Two dictionaries are validated against the `Student` class:
     - `json_student_data` uses camelCase.
     - `student_data_with_snake_case_support` uses snake_case.
   - Both formats are successfully converted to a `Student` object due to alias support.

5. **Object Creation and Output**:
   - The `model_validate` method validates the input dictionary and creates a `Student` object.
   - The `model_dump` method outputs the object data in Python's dictionary format.
   - Attribute access is demonstrated using `first_name`, `last_name`, and `student_number`.

---

### Example Use Case:

This approach is ideal for:
- Processing API responses with JSON data in camelCase.
- Allowing Pythonic snake_case naming in your internal codebase while seamlessly handling camelCase from external sources.

---

### Sample Output:

For the two input dictionaries, the output will be:

```python
{'first_name': 'John', 'last_name': 'Doe', 'student_number': 1234}
John
Doe
1234
{'first_name': 'John', 'last_name': 'Doe', 'student_number': 1234}
