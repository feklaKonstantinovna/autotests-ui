import pytest

@pytest.mark.performance
def test_memory_usage():
    pass

@pytest.mark.slow
class TestStress:
    def test_stress_1(self):
        pass

    @pytest.mark.performance
    def test_stress_2(self):
        pass
