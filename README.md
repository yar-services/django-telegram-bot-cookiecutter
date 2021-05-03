# django-telegram-bot-cookiecutter

Bleeding edge `django2.2` template focused on developing telegram bots.

Based on original [wemake-django-template](https://github.com/wemake-services/wemake-django-template). Thanks!
---

## Features

- Supports latest `python3.8+`
- [`poetry`](https://github.com/python-poetry/poetry) for managing dependencies
- [`mypy`](https://mypy.readthedocs.io) and [`django-stubs`](https://github.com/typeddjango/django-stubs) for static typing
- [`pytest`](https://pytest.org/) and [`hypothesis`](https://github.com/HypothesisWorks/hypothesis) for unit tests
- [`flake8`](http://flake8.pycqa.org/en/latest/) and [`wemake-python-styleguide`](https://wemake-python-styleguide.readthedocs.io/en/latest/) for linting
- [`docker`](https://www.docker.com/) for development, testing, and production
- [`sphinx`](http://www.sphinx-doc.org/en/master/) for documentation
- [`Gitlab CI`](https://about.gitlab.com/gitlab-ci/) with full `build`, `test`, and `deploy` [pipeline configured by default](https://gitlab.com/sobolevn/wemake-django-template/-/pipelines)
- [`Caddy`](https://caddyserver.com/) with [`https`](https://caddyserver.com/docs/automatic-https) and `http/2` turned on by default

## Installation

Firstly, you will need to install [dependencies](https://cookiecutter.readthedocs.io/en/latest/):

```bash
pip install cookiecutter jinja2-git
```

Then, create a project itself:

```bash
cookiecutter gh:yar-services/django-telegram-bot-cookiecutter
```

## License

MIT. See [LICENSE](https://github.com/yar-services/django-telegram-bot-cookiecutter/blob/master/LICENSE) for more details.
