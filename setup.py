# -*- coding: UTF-8 -*-
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_mail_template',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Application for creating mails templates with context '
                'variables. There is a double mapping between a mail template '
                'and process configuration so is possible to change the used '
                'mail template in a process at run time with admin GUI',
    long_description=README,
    long_description_content_type='text/markdown',
    url='',
    author='Vicente Ramos Garcia',
    author_email='vramosga@gmail.com',
    classifiers=[
        # 'Development Status :: 1 - Planning'
        # 'Development Status :: 2 - Pre-Alpha'
        # 'Development Status :: 3 - Alpha'
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable'
        # 'Development Status :: 6 - Mature'
        # 'Development Status :: 7 - Inactive'
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Communications :: Email',
    ],
)
