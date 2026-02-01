import sys
sys.path.append("src") 

import beam

def test_bending_moment():
    M = beam.bending_moment(1000, 2)
    assert M == 500


def test_safety_factor():
    SF = beam.safety_factor(250, 50)
    assert SF == 5
