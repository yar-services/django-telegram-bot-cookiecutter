
import pytest


@pytest.fixture()
def context():
    """Creates default prompt values."""
    return {
        'project_name': 'test-bot',
        'project_verbose_name': 'Test Bot',
        'project_domain': 'myapp.com',
        'organization': 'yar-services',
    }
