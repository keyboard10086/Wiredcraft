from ..util import APIUtil, ConfigPaser
import pytest
from pytest import *
from . import get_countires_api_url


@pytest.fixture(autouse=False, scope="module")
def api_specific_fixture():
    print("this gets executed before the current test suite.")
    pass
    print("this gets executed after the current test suite.")

@pytest.fixture(autouse=False, scope="function")
def api_specific_fixture():
    print("this gets executed before each test case.")
    pass
    print("this gets executed after each test case.")

@pytest.fixture(autouse=False)
def api_specific_fixture():
    print("this gets executed before testcases that used this fixture.")
    pass
    print("this gets executed after testcases that used this fixture.")

@pytest.mark.testcase1
def test_get_all_countries_with_json_format():
    params = "?format=json"
    req = APIUtil.RequestOperation(get_countires_api_url+params)
    res, code = req.set_request_method("get").send_request_and_get_json_response()
    #print(res)
    assert code == 200
    assert res[0]['page'] == 1
    assert res[0]['pages'] == 6
    assert res[0]['per_page'] == '50'
    assert res[0]['total'] == 299
    assert len(res[1]) == 50

@pytest.mark.testcase2
def test_get_specified_page_and_number_countries_with_json_format():
    params = "?format=json&per_page=2&page=15"
    req = APIUtil.RequestOperation(get_countires_api_url+params)
    res, code = req.set_request_method("get").send_request_and_get_json_response()
    print(res)
    assert code == 200
    assert res[0]['page'] == 15
    assert res[0]['pages'] == 150
    assert res[0]['per_page'] == '2'
    assert res[0]['total'] == 299
    assert len(res[1]) == 2
    pass