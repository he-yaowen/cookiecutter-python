import random
from chance import chance

license_stubs = {
    'Apache-2.0': 'Apache License',
    'BSD-3-Clause': 'BSD License',
    'GPL-3.0': 'GNU General Public License',
    'MIT': 'MIT License',
    'MPL-2.0': 'Mozilla Public License'
}


def test_bake_license(cookies):
    for license_id, license_stub in license_stubs.items():
        result = cookies.bake(extra_context={'license_id': license_id})

        assert license_stub in result.project_path.joinpath('LICENSE').read_text()

        for key in license_stubs.keys():
            assert not result.project_path.joinpath(f'LICENSE.{key}').exists()


def test_bake_readme(cookies):
    license_id = chance.pickone([key for key in license_stubs.keys()])

    context = {
        'project_name': f'{chance.word().capitalize()} {chance.word().capitalize()}',
        'project_slug': chance.word(),
        'project_description': chance.sentence(),
        'author_email': chance.email(),
        'license_id': license_id,
        'license_fullname': chance.name(),
        'license_year': random.randint(2000, 2022)
    }

    result = cookies.bake(extra_context=context)

    readme = result.project_path.joinpath('README.md').read_text()

    assert context['project_name'] in readme
    assert context['project_description'] in readme

    assert license_stubs[license_id] in readme
    assert f'Copyright (C) {context["license_year"]} {context["license_fullname"]} <{context["author_email"]}>' in readme
