"""Creating a client like this abstracts away the low-level details of making API requests, 
making it easier to use the API and reducing the amount of code needed to interact with it. 
This can lead to improved readability, maintainability, and overall code quality."""

from urllib.parse import urljoin
import requests
from django.conf import settings

session = requests.Session()
session.auth = (settings.DYTE_ORG_ID, settings.DYTE_API_KEY)

class DyteAPIClient(object):
    """This class creates Create new meeting, Add participant to meeting and Refresh participant token."""
    def __init__(self):
        pass

    @classmethod
    def _create_url(cls, path):
        return urljoin(settings.DYTE_API_BASE_URL, path)

    @classmethod
    def _fetch(cls, request: requests.Request):
        prepared_request = session.prepare_request(request)
        response = session.send(prepared_request)
        response.raise_for_status()
        return response.json()["data"]

    @classmethod
    def create_meeting(
        cls, title: str, preferred_region: str, record_on_start: bool
    ) -> dict:
        data = {
            "title": title,
            "preferred_region": preferred_region,
            "record_on_start": record_on_start,
        }
        request = requests.Request(
            method="POST",
            url=cls._create_url("meetings"),
            json=data,
        )
        return cls._fetch(request)

    @classmethod
    def add_participant(
        cls, meeting_id: str, name: str, preset_name: str, custom_participant_id: str
    ) -> dict:
        data = {
            "name": name,
            "preset_name": preset_name,
            "custom_participant_id": custom_participant_id,
        }
        request = requests.Request(
            method="POST",
            url=cls._create_url(f"meetings/{meeting_id}/participants"),
            json=data,
        )
        return cls._fetch(request)

    @classmethod
    def refresh_participant_token(cls, meeting_id: str, participant_id: str) -> dict:
        request = requests.Request(
            method="POST",
            url=cls._create_url(
                f"meetings/{meeting_id}/participants/{participant_id}/token"
            ),
        )
        return cls._fetch(request)