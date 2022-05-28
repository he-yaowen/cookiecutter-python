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


def test_bake_context(cookies):
    license_id = chance.pickone([key for key in license_stubs.keys()])

    context = {
        'project_name': f'{chance.word().capitalize()} {chance.word().capitalize()}',
        'project_slug': chance.word(),
        'project_version': f'{random.randint(0, 9)}.{random.randint(0, 9)}.{random.randint(0, 9)}',
        'project_description': chance.sentence(),
        'author_name': chance.name(),
        'author_email': chance.email(),
        'license_id': license_id,
        'license_fullname': chance.name(),
        'license_year': random.randint(2000, 2022),
        'python_version': chance.pickone(['3.7', '3.8', '3.9', '3.10', '3.11'])
    }

    result = cookies.bake(extra_context=context)

    readme = result.project_path.joinpath('README.md').read_text()

    assert context['project_name'] in readme
    assert context['project_description'] in readme

    assert license_stubs[license_id] in readme
    assert f'Copyright (C) {context["license_year"]} {context["license_fullname"]} <{context["author_email"]}>' in readme

    pyproject = result.project_path.joinpath('pyproject.toml').read_text()

    assert context['project_description'] in pyproject
    assert context['project_version'] in pyproject
    assert context['author_name'] in pyproject
    assert context['author_email'] in pyproject
    assert context['python_version'] in pyproject


def test_bake_package(cookies):
    result = cookies.bake()
    package = result.project_path.joinpath(f'src/{result.context["project_slug"]}')
    assert package.exists()

    assert result.context['project_slug'] in package.joinpath('__init__.py').read_text()


def test_bake_with_click(cookies):
    result = cookies.bake(extra_context={'with_click': 'yes'})

    assert 'click' in result.project_path.joinpath('pyproject.toml').read_text()
    assert result.project_path.joinpath(f'src/{result.context["project_slug"]}/__main__.py').exists()

    result = cookies.bake(extra_context={'with_click': 'no'})

    assert 'click' not in result.project_path.joinpath('pyproject.toml').read_text()
    assert not result.project_path.joinpath(f'src/{result.context["project_slug"]}/__main__.py').exists()
