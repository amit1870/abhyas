import pytest

class TestNames:

    @pytest.fixture(scope="class")
    def bhagwan_ke_nam(self):
        return ['sitaram', 'radhakrishna', 'laxminath', 'keshav' ,'madhav']

    def test_list_length_one(self, bhagwan_ke_nam):
        assert len(bhagwan_ke_nam) == 5

    def test_name_in_list(self, bhagwan_ke_nam):
        assert 'sitaram' in bhagwan_ke_nam
        assert 'radhakrishna' in bhagwan_ke_nam

    def add_name_to_list(self, bhagwan_ke_nam):
        bhagwan_ke_nam.append('ramanuj')
        bhagwan_ke_nam.append('urmilalaxman')

    def test_list_length_two(self, bhagwan_ke_nam):
        self.add_name_to_list(bhagwan_ke_nam)
        assert len(bhagwan_ke_nam) > 5

    def test_name_in_list_two(self, bhagwan_ke_nam):
        assert 'sitaram' in bhagwan_ke_nam
        assert 'urmilalaxman' in bhagwan_ke_nam

class TestFixtureScope:

    def pytest_addoption(parser):
        parser.addinitvalue_line("markers" , "scoped: to test fixture scope")

    @pytest.mark.xfail(reason="fixture with scope=class are not available for other classes")
    def test_name_in_list(self, bhagwan_ke_nam):
        assert len(bhagwan_ke_nam) > 0

