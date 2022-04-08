import pytest
import student 

def test_default():
    assert student.initials(["Steve Rogers", "Tony Stark", "Bruce Banner"]) == ["SR", "TS", "BB"]

def test_business_department():
    assert student.initials(["Austin Scarpelli", "Andrea Brule", "Rosarie Brazier"])==['AS','AB','RB']

