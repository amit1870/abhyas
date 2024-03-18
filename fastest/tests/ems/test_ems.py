import pytest

from src.ems.emp_mgmt import empmgr

@pytest.mark.cmd
def test_employee_with_cmd(employee):
    assert employee.id > 0

@pytest.mark.empadd
def test_employee_add(employee):
    assert employee.id == empmgr.add(employee)

@pytest.mark.empedit
def test_employee_edit_one(employee_id, employee_details):
    assert employee_id == empmgr.edit(employee_id, **employee_details)

@pytest.mark.empedit
def test_employee_edit_two(employee_id, employee_details):
    non_existing_employee_id = 100
    with pytest.raises(AssertionError):
        assert employee_id == empmgr.edit(non_existing_employee_id, **employee_details)

@pytest.mark.empdelete
def test_employee_delete_one(employee_id):
    assert employee_id == empmgr.delete(employee_id)

@pytest.mark.empdelete
def test_employee_delete_two(employee_id):
    assert ('error in delete employee',) == empmgr.delete(employee_id)

@pytest.mark.empmock
def test_employee_add_mock(employee, monkeypatch):
    def mockadd():
        return employee.id

    monkeypatch.setattr(empmgr, 'add', mockadd)

    assert employee.id == empmgr.add()

@pytest.mark.empmock
def test_employee_edit_mock(employee):
    assert employee.id == empmgr.edit(employee.id)


