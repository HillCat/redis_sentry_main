import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    version="1.0",
    name="redis_sentry",
    packages=find_packages(),
    py_modules=["redis_sentry"],
    author="Maximiliano Lira Del Canto",
    install_requires=[
        'openai-whisper @ git+https://github.com/openai/whisper.git@main#egg=openai-whisper'
    ],
    description="Generate subtitles for videos using sentry",
    entry_points={
        'console_scripts': ['redis_sentry=redis_sentry.cli:main'],
    },
    include_package_data=True,
)
