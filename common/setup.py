from setuptools import setup, find_packages

setup(
    name='pulp_ostree_common',
    version='1.0.0',
    packages=find_packages(),
    url='http://www.pulpproject.org',
    license='GPLv2+',
    author='Pulp Team',
    author_email='pulp-list@redhat.com',
    description='common code for pulp\'s ostree support',
)
