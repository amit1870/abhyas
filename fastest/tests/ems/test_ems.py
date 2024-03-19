import pytest

from src.ems.emp_mgmt import empmgr

@pytest.mark.skip
def test_ems_db_running(is_db_running):
    assert is_db_running


@pytest.mark.skip
def test_empty_db(empty_db):
    with open(empty_db) as fp:
        content = fp.read()

    assert 'empid,fsname,lsname,dprtmt,salary,status,limit' in content

@pytest.mark.skip
def test_employee_add(employee):
    assert employee.id == empmgr.add(employee)

@pytest.mark.skip
def test_employee_edit(employee_id, employee_details):
    assert employee_id == empmgr.edit(employee_id, **employee_details)

def test_employee_add_mock(employee, monkeypatch):
    def add(employee):
        return 202

    monkeypatch.setattr(empmgr, 'add', add)

    employee_id = 202

    assert employee_id == empmgr.add(employee)

def test_employee_edit_mock(employee_id, employee_details, monkeypatch):
    def edit(employee_id, **employee_details):
        return 202

    monkeypatch.setattr(empmgr, 'edit', edit)

    employee_id = 202

    assert employee_id == empmgr.edit(employee_id, **employee_details)

