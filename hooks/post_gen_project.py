import os
from glob import glob

license_id = '{{ cookiecutter.license_id }}'

if license_id != 'None':
    os.rename('LICENSE.{{ cookiecutter.license_id }}', 'LICENSE')

for license_file in glob('LICENSE.*'):
    os.unlink(license_file)
