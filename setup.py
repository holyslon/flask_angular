"""
Flask-Angular
--------------

Add Flask-Script for generating AngularJS files in CoffeeScript


"""
import sys
from setuptools import setup

# Hack to prevent stupid TypeError: 'NoneType' object is not callable error on
# exit of python setup.py test # in multiprocessing/util.py _exit_function when
# running python setup.py test (see
# https://github.com/pypa/virtualenv/pull/259)
try:
    import multiprocessing
except ImportError:
    pass

install_requires = ['Flask-Script']

setup(
    name='Flask-Angular',
    version='0.0.1-dev',
    url='http://github.com/holyslon/flask_angular',
    license='BSD',
    author='Anton Onikiichuk',
    author_email='anton@onikiychuk.com',
    description='Add Flask-Script for generating AngularJS files in CoffeeScript',
    long_description=__doc__,
    packages=[
        'flask_angular'
    ],
    package_data={'flask_angular': ['flask_angular/templates/*']},
    include_package_data=True,
    test_suite='nose.collector',
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    tests_require=[
        'nose',
        'mock'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)