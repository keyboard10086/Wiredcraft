import copy
import requests


class RequestOperation():

    def __init__(self, url):
        self.session = requests.Session()
        self.request = requests.Request(url=url)

    def construct_header(self, header_dict={}, header_key=None, header_value=None):
        if header_key is not None and header_value is not None:
            header_dict[header_key] = header_value
        return header_dict

    def set_request_method(self, method="get"):
        self.request.method = method
        return self

    def set_request_header(self, header={}):
        request_header = copy.deepcopy(self.request.headers)
        for headerkey, headervalue in header.items():
            if not headerkey in request_header:
                self.request.headers[headerkey] = headervalue
        return self

    def set_request_params(self, params=""):
        self.request.params = params
        return self

    def set_request_body(self,  content_type="json", body={}):
        if content_type == "json":
            self.request.json = body
        else:
            self.request.data = body
        return self

    def set_upload_file(self, file_obj={}):
        self.request.files = file_obj
        return self

    def send_request_and_get_json_response(self):
        prepared_request = self.session.prepare_request(self.request)
        response = self.session.send(prepared_request)
        # print(response.json())
        # print(response.headers)
        # print(response.cookies.items())
        # return self
        return response.json(), response.status_code

    def send_request_and_get_text_response(self):
        print(self.request.headers)
        print(self.request.data)
        prepared_request = self.session.prepare_request(self.request)
        response = self.session.send(prepared_request)
        return response.text, response.status_code

    def set_form_flag(self, form_flag:bool):
        if form_flag:
            self.request.headers["x-www-form-urlencoded"] = "true"
        return self