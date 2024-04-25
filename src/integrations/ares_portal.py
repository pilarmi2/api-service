import os

import requests


class AresPortal:
    url = f'{os.environ["ARES"]}'
    def get_municipality_name(self, municipality_id: str) -> str:
        """
        Retrieves the name of a municipality based on its ID.

        Args:
            municipality_id (str): The ID of the municipality to retrieve the name for.

        Returns:
            str: The name of the municipality.
        """
        url = f'{self.url}/{municipality_id}'
        response = requests.get(url).json()

        return response['sidlo']['nazevObce']
