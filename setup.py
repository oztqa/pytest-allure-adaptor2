import os
from setuptools import setup

PACKAGE = "pytest-allure-adaptor2"

install_requires = [
    "lxml>=3.2.0",
    "pytest>=2.7.3",
]


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def main():
    setup(
        name=PACKAGE,
        version_format='{tag}',
        description=("Plugin for py.test to generate allure xml reports"),
        author="pupssman",
        author_email="pupssman@yandex-team.ru",
        packages=["allure"],
        url="https://github.com/allure-framework/allure-pytest",
        entry_points={'pytest11': ['allure_adaptor = allure.pytest_plugin']},
        install_requires=install_requires,
        setup_requires=['setuptools-git-version'],
    )


if __name__ == '__main__':
    main()
