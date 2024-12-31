## Description

This code defines a **`Student`** class using the latest version of **Pydantic**, leveraging the `ConfigDict` for configuring model behavior. The class is designed to validate and transform incoming data, such as JSON objects, into structured Python objects. It supports aliasing and allows handling of extra fields flexibly.

---

### Key Features:

1. **Class Definition**:
   - The `Student` class inherits from `BaseModel` in Pydantic.
   - Fields include `first_name`, `last_name`, and `student_number`, with aliases defined (`firstName`, `lastName`, `studentNumber`) for compatibility with camelCase JSON.

2. **`ConfigDict` Usage**:
   - `model_config` replaces the deprecated `Config` subclass for setting model configurations in newer Pydantic versions.
   - The configuration options demonstrated:
     - `populate_by_name=True`: Allows attribute population using aliases.
     - `extra="ignore"`: Ignores additional fields in the input data that are not defined in the model.
     - Commented options for `extra="forbid"` (disallows extra fields) and `extra="allow"` (permits and includes extra fields in the output).

3. **Alias Handling**:
   - The `Field` function specifies aliases for attributes, enabling seamless handling of camelCase keys from external sources.

4. **Validation and Transformation**:
   - Input dictionaries are validated using `Student.model_validate`. Two examples are demonstrated:
     - `json_student_data` uses camelCase.
     - `student_data_with_snake_case_support` uses snake_case.
   - Both formats are successfully converted to a `Student` object due to alias support.

5. **Deprecated Config Style**:
   - The older `Config` subclass is commented out, demonstrating its replacement with `ConfigDict`.

---

### Example Use Case:

This approach is ideal for:
- Processing API responses where data fields might include extra or unexpected fields.
- Supporting camelCase JSON while maintaining Pythonic snake_case internally.
- Flexible configurations for handling strictness in input data.

---

### Sample Output:

For the input data, the output will be:

```python
{'first_name': 'John', 'last_name': 'Doe', 'student_number': 254456}
John
Doe
254456
{'first_name': 'John', 'last_name': 'Doe', 'student_number': 254123}
