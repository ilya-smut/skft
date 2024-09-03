from setuptools import setup

setup(
    name='skft',
    description="Simple package to parse football schedule for today from sky sports",
    long_description=open("README.md", 'r', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/ilya-smut/skft",
    project_urls={
        "Source Code": "https://github.com/ilya-smut/skft",
    },
    author="Ilya Smut",
    author_email="ilya.smut.off.g@gmail.com",
    license="GPL-3.0 license",
    version='0.0.1',
    packages=['skft'],
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    entry_points={
        'console_scripts': [
            'skft = skft.football:run',
        ],
    },
)