import os

import requests


class AresPortal:
    def get_municipality_name(self, municipality_id: str) -> str:
        url = f'{os.environ["ARES"]}/{municipality_id}'
        response = requests.get(url).json()

        return response['sidlo']['nazevObce']
