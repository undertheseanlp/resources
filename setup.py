from setuptools import setup

install_requires = [
    'Jinja2==2.10.1',
    'Click>=6.0',
]
tests_require = [

]
setup_requires = [
]

version = '1.0.0'
setup(
    name='vietnamese',
    version=version,
    description="Vietnamese NLP Data",
    long_description='Vietnamese NLP Data',
    author="Vu Anh",
    author_email='anhv.ict91@gmail.com',
    url='https://github.com/undertheseanlp/underthesea',
    packages=[
        'vietnamese',
    ],
    package_dir={'vietnamese': 'vietnamese'},
    entry_points={
        'console_scripts': [
            'ts=vietnamese.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=install_requires,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='underthesea,vietnamese',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=tests_require,
    setup_requires=setup_requires
)
