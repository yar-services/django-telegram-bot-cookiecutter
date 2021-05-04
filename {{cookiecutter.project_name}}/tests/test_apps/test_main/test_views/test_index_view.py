from django.test import Client
from django.urls import reverse


def test_main_page(client: Client, main_heading: str) -> None:
    """This test ensures that bot page works."""
    response = client.get('/')

    assert response.status_code == 200
    assert main_heading in str(response.content)


def test_hello_page(client: Client, main_heading: str) -> None:
    """This test ensures that hello page works."""
    response = client.get(reverse('bot:hello'))

    assert response.status_code == 200
    assert main_heading in str(response.content)
