import pytest
from project import certificate_grades, template_choise, check_input_csv, check

def main():
    test_certificate_grades()
    test_check_input_csv()
    test_check()
    test_template_choise()

def test_certificate_grades():
    assert certificate_grades("with_grades.png", "grades.csv") == "Certificate is finished"

def test_check_input_csv():
    assert check_input_csv("grades.csv") == True
    assert check_input_csv("with_grades") == None
    assert check_input_csv("with_grades.png") == None
    with pytest.raises(FileNotFoundError):
        check_input_csv("aaa.csv")
    with pytest.raises(FileNotFoundError):
        check_input_csv("sadscs44.csv")

def test_check():
    assert check("with_grades.png") == "grade"
    assert check("without_grades.png") == "certificate"
    assert check("aaaa") == None

def test_template_choise():
    assert template_choise(1) == True
    assert template_choise(2) == True
    assert template_choise(0) == None

if __name__ == "__main__":
    main()