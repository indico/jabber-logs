from setuptools import setup, find_packages

setup(
    name="jabber_logs",
    version="0.1",
    author="Indico Team",
    author_email="indico-team@cern.ch",
    description=("Jabber Logs WebApp"),
    license="GPL3",
    keywords="jabber",
    url="http://indico-software.org",
    packages=find_packages(),
    long_description=open('README.md', 'r').read(),
    include_package_data=True,
    package_data={
    },
    install_requires=['Flask==0.10.1', 'python-dateutil==2.2']
    )
