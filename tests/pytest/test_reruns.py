import pytest
import random


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_reruns():
      assert random.choice([True, False])
