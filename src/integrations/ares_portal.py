import requests


class AresPortal:
    def get_municipality_name(self, municipality_id: str) -> str:
        url = f'https://wwwinfo.mfcr.cz/cgi-bin/ares/darv_std.cgi?ico={municipality_id}'
        response = requests.get(url)

        print(response.text)

        return "Prague"
