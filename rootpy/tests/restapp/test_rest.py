import pytest

from src.restapp.api import restapi

class TestRestAPI:

    def test_get(self):
        assert restapi.get() == 200

    def test_post(self):
        assert restapi.post() == 201

