# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

{% if cookiecutter.license_id != 'None' %}
## License

Copyright (C) {{ cookiecutter.license_year }} {{ cookiecutter.license_fullname }} <{{ cookiecutter.author_email }}>

{%- if cookiecutter.license_id == 'Apache-2.0' %}

Apache License, Version 2.0, see [LICENSE](./LICENSE).
{%- elif cookiecutter.license_id == 'BSD-3-Clause' %}

The 3-Clause BSD License, see [LICENSE](./LICENSE).
{%- elif cookiecutter.license_id == 'GPL-3.0' %}

The GNU General Public License (GPL) version 3, see [LICENSE](./LICENSE).
{%- elif cookiecutter.license_id == 'MIT' %}

MIT License, see [LICENSE](./LICENSE).
{%- elif cookiecutter.license_id == 'MPL-2.0' %}

Mozilla Public License 2.0, see [LICENSE](./LICENSE).
{%- endif %}
{% endif %}
