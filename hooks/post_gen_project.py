import os
from glob import glob

license_id = '{{ cookiecutter.license_id }}'
with_click = '{{ cookiecutter.with_click }}'
with_pyinstaller = '{{ cookiecutter.with_pyinstaller }}'

if license_id != 'None':
    os.rename('LICENSE.{{ cookiecutter.license_id }}', 'LICENSE')

for license_file in glob('LICENSE.*'):
    os.unlink(license_file)

if with_click == 'no':
    os.unlink('src/{{ cookiecutter.project_slug }}/__main__.py')

if with_pyinstaller == 'no':
    os.unlink('{{ cookiecutter.project_slug }}.spec')
