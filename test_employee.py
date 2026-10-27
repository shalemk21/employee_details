from emp_details import employee_details

def test_employee_details():
    result = employee_details("RJ", "00000", "Engineering", "75000")

    expected = "Name: RJ\nEmployee ID: 00000\nDepartment: Engineering\nSalary: $75000"
    assert result == expected