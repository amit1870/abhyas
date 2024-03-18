import pytest

from src.ems.emp_mgmt import Employee

def pytest_addoption(parser):
    parser.addoption("--id", action="store", type=int, help="employee id")
    parser.addoption("--action", choices=['add', 'edit', 'delete', 'view'], default='view')
    parser.addoption("--filtter", choices=['active', 'deleted', 'all'], default='active')
    parser.addoption("--fsname", help="first name", default='')
    parser.addoption("--lsname", help="last name", default='')
    parser.addoption("--dprtmt", help="department", default='bose')
    parser.addoption("--salary", help="salary", default=0, type=int)


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "cmd: test for command line params"
    )

    config.addinivalue_line(
        "markers",
        "empadd: test for adding employee"
    )
    config.addinivalue_line(
        "markers",
        "empedit: test for editing employee"
    )
    config.addinivalue_line(
        "markers",
        "empdelete: test for deleting employee"
    )
    config.addinivalue_line(
        "markers",
        "empview: test for viewing employee"
    )
    config.addinivalue_line(
        "markers",
        "empmock: test for mocking employee add/delete/edit/view"
    )
    config.addinivalue_line(
        "markers",
        "bulk: test for adding employee in bulk"
    )


@pytest.fixture
def employee(request):
    empid = request.config.option.id
    fsname = request.config.option.fsname
    lsname = request.config.option.lsname
    dprtmt = request.config.option.dprtmt
    salary = request.config.option.salary

    return Employee(empid, fsname, lsname, dprtmt, salary)


@pytest.fixture(autouse=True)
def employee_id(request):
    empid = request.config.option.id
    return empid

@pytest.fixture
def employee_action(request):
    action = request.config.option.action
    return action

@pytest.fixture
def employee_details(request):
    empdict = {}
    empdict['fsname'] = request.config.option.fsname
    empdict['lsname'] = request.config.option.lsname
    empdict['dprtmt'] = request.config.option.dprtmt
    empdict['salary'] = request.config.option.salary

    return empdict


