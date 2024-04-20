from setuptools import find_packages, setup

from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        for line in file_obj:
            requirement = line.strip()
            requirements.append(requirement)

    return requirements

setup(
    name='Web Scraping',
    version='0.0.1',
    author='Vinothkumar',
    author_email='mailforvinoth97@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
