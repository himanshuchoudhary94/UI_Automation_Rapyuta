import os

import requests

class GWMClientException(BaseException):
    def __init__(self, message):
        self.message = message


class GWMClient:
    def __init__(
            self,
            core_url=os.environ.get('GWM_CORE_URL', 'https://himanshutrail11-gwm-kqdbp.ep-r.io'),
            interface_url=os.environ.get('GWM_INTERFACE_URL', 'https://himanshutrail11-gbc-kqdbp.ep-r.io:443'),
            # site='',
            retry_limit=3):
        self.core_url = core_url
        self.interface_url = interface_url
        self.retry_limit = retry_limit
        self.headers = {
            'Authorization': 'Token autobootstrap',
            'X-RRAMR-Site': '2',
            'X-RRAMR-ORG': '1'
        }

    def create_payload_work(self, pick, drop, priority=1, tracking_id=''):
        data = {
            'type': 'PAYLOAD_MOVE',
            'src_spots': pick,
            'dest_spot': drop,
            'priority': priority,
            'ext_tracking_id': tracking_id
        }

        return self._execute('POST', self.core_url + '/v1/work', data)

    def _execute(self, method, url, data=None, **kwargs):
        retry_count = 0
        error_message = None
        while retry_count < self.retry_limit:
            try:
                res = requests.request(method, url, json=data, headers=self.headers, params=kwargs, timeout=3)
                # Raise exception if status_code is 4xx or 5xx
                res.raise_for_status()
                try:
                    return res.json()
                except ValueError:  # Handle JSONDecodeError
                    return None
            except requests.exceptions.RequestException as e:
                retry_count += 1
                error_message = e

        raise GWMClientException(f"Error occurred for URL {url}: {error_message}")