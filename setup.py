from setuptools import setup, find_packages
from setuptools.command.egg_info import egg_info


class egg_info_ex(egg_info):
    """Includes license file into `.egg-info` folder."""

    def run(self):
        # don't duplicate license into `.egg-info` when building a distribution
        if not self.distribution.have_run.get('install', True):
            # `install` command is in progress, copy license
            self.mkpath(self.egg_info)
            self.copy_file('LICENSE.txt', self.egg_info)

        egg_info.run(self)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'automaticonn',
    version = '0.0.3',
    author = 'Marko Mandic',
    author_email = 'mandicm223@gmail.com',
    license_files = ('LICENSE',),
    description = 'CLI tool that lets you to automaticly manage your AWS services without leaving terminal.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/JaSamLudiMoskri/aws_automation_BOT',
    py_modules = ['automaticon', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        automaticon=automaticon:main
    '''
)