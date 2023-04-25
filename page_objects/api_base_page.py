import requests
import config


class APIUtils:

    def __init__(self, base_url: str | None = None, headers: dict | None = None):
        if config.BASE_URL:
            self.BASE_URL = config.BASE_URL
        else:
            self.BASE_URL = base_url

        if config.HEADERS:
            self.HEADERS = config.HEADERS
        else:
            self.HEADERS = headers

    def _get(self, endpoint_url: str, params_data: dict | None = None) -> tuple:
        """
        which returns a representational view of a resource's contents and data.
        :param endpoint_url: url pointing to endpoint
        :param params_data: dictionary data for params
        :return: tuple contains response data in first index and response status code in second index
        """
        resp = requests.get(self.BASE_URL + endpoint_url, params=params_data, headers=self.HEADERS)
        return resp.json(), resp.status_code

    def _post(self, endpoint_url: str, payload_json: dict | None = None) -> tuple:
        """
        Every POST method call should result in a new object being created (or possibly deleted) in the database.
        :param endpoint_url: url pointing to endpoint
        :param payload_json: dictionary payload for new object creation
        :return: tuple contains response data in first index and response status code in second index
        """
        resp = requests.post(self.BASE_URL + endpoint_url, headers=self.HEADERS, json=payload_json)
        return resp.json(), resp.status_code

    def _delete(self, endpoint_url: str, payload_json: dict | None = None) -> tuple:
        """
         A DELETE request should accept a unique identifier to remove only one data
        :param endpoint_url: url pointing to endpoint
        :param payload_json: dictionary payload for new object creation
        :return: tuple contains response data in first index and response status code in second index
        """
        resp = requests.delete(self.BASE_URL + endpoint_url, headers=self.HEADERS, json=payload_json)
        return resp.json(), resp.status_code

    def _put(self, endpoint_url: str, payload_json: dict | None = None) -> tuple:
        """
        PUT can still be used for creating objects, although since it is idempotent, repeatedly executing the same
        request will have the same end result as the first time.
        :param endpoint_url: url pointing to endpoint
        :param payload_json: dictionary payload for new object creation
        :return: tuple contains response data in first index and response status code in second index
        """
        resp = requests.put(self.BASE_URL + endpoint_url, headers=self.HEADERS, json=payload_json)
        return resp.json(), resp.status_code
