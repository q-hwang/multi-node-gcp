from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'accelerate',
    'datasets',
    'transformers',
    'deepspeed',
]

setup(
    name='trainer',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='My training application.',
    package_data={
        "": [
            "*.json",
            "*.jsonl",
            "*.txt",
            "*.tsv",
            "*.csv",
            "*.npz",
            "*.ckpt",
            "*.gz",
            "*.zip",
            "*.yaml",
            "*.pkl",
        ]
    },
)