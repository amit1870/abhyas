import pytest

from pathlib import Path


@pytest.fixture
def get_dbpath():
    return Path.home() /  'abhyas/fastest/tests/pyapp' / 'db.csv'


@pytest.fixture
def get_file_data(get_dbpath):
    with open(get_dbpath) as db:
        yield db.read()

    # remove filepath

    Path.unlink(get_dbpath, missing_ok=True)


def write_content_to_db(dbpath, content):
    with open(dbpath, 'w') as db:
        db.write(content)

    return dbpath


def test_db_write_permission(get_dbpath):
    content = 'name,age'
    assert get_dbpath == write_content_to_db(get_dbpath, content)

def test_verify_content(get_file_data):
    content = get_file_data
    assert 'name' in content or 'age' in content



