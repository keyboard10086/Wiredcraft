from ..util import APIUtil, ConfigPaser
import pytest
from pytest import *
from . import get_countires_api_url, get_countrues_api_url_Chinese

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
def test_get_country_details_with_country_id():
    params = "/FIN?format=json"
    req = APIUtil.RequestOperation(get_countires_api_url+params)
    res, code = req.set_request_method("get").send_request_and_get_json_response()
    print(res)
    assert code == 200
    pages = res[0]
    assert pages['page'] == 1
    assert pages['pages'] == 1
    assert pages['per_page'] == '50'
    assert pages['total'] == 1
    assert len(pages) == 1

    regions = res[1]
    assert regions[0]['id'] == 'FIN'
    assert regions[0]['iso2Code'] == 'FI'
    assert regions[0]['name'] == 'Finland'

@pytest.mark.testcase1
def test_get_country_details_with_country_id():
    params = "/FIN?format=json"
    req = APIUtil.RequestOperation(get_countires_api_url+params)
    res, code = req.set_request_method("get").send_request_and_get_json_response()
    assert code == 200
    pages = res[0]
    assert pages['page'] == 1
    assert pages['pages'] == 1
    assert pages['per_page'] == '50'
    assert pages['total'] == 1

    regions = res[1]
    assert len(regions) == 1
    assert regions[0]['id'] == 'FIN'
    assert regions[0]['iso2Code'] == 'FI'
    assert regions[0]['name'] == 'Finland'

@pytest.mark.testcase2
def test_get_country_details_with_country_iso2code():
    params = "/FI?format=json"
    req = APIUtil.RequestOperation(get_countires_api_url+params)
    res, code = req.set_request_method("get").send_request_and_get_json_response()
    print(res)
    assert code == 200
    pages = res[0]
    assert pages['page'] == 1
    assert pages['pages'] == 1
    assert pages['per_page'] == '50'
    assert pages['total'] == 1

    regions = res[1]
    assert len(regions) == 1
    assert regions[0]['id'] == 'FIN'
    assert regions[0]['iso2Code'] == 'FI'
    assert regions[0]['name'] == 'Finland'

@pytest.mark.testcase3
def test_get_country_details_with_country_fullname():
    params = "/Finland?format=json"
    req = APIUtil.RequestOperation(get_countires_api_url+params)
    res, code = req.set_request_method("get").send_request_and_get_json_response()
    print(res[0])
    assert code == 200
    # this API does not support query by country full name
    assert res[0]['message'][0]['key'] == "Invalid value"
    assert res[0]['message'][0]['value'] == "The provided parameter value is not valid"

@pytest.mark.testcase4
def test_get_country_details_with_country_Chinese_name():
    params = "?format=json&per_page=1"
    req = APIUtil.RequestOperation(get_countrues_api_url_Chinese + params)
    res, code = req.set_request_method("get").send_request_and_get_json_response()
    print(res)
    assert code == 200
    regions = res[1]
    assert regions[0]['name'] == '阿鲁巴'
