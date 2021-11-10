import requests


class SocProofAPI:
    def __init__(self, api_key):
        self._api_key = api_key
        self._session = requests.Session()
        self._url = "https://soc-proof.su/api/v2"

    def services(self):
        result = self._session.get(f'{self._url}?action=services&key={self._api_key}')
        return result.json()

    def balance(self):
        result = self._session.get(f'{self._url}?action=balance&key={self._api_key}')
        return result.json()

    def add_order(self, service, link, quantity):
        result = self._session.get(
            f"{self._url}?action=add&service={service}&link={link}&quantity={quantity}&key={self._api_key}")
        return result.json()

    def cancel_order(self, order):
        result = self._session.get(f"{self._url}?action=cancel&order={order}&key={self._api_key}")
        return result.json()

    def order_status(self, order):
        result = self._session.get(f"{self._url}?action=status&orders={order}&key={self._api_key}")
        return result.json()
