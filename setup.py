from setuptools import setup, find_packages
setup(
  name='pyvcroid2',
  version='0.2.1',
  author='Nkyoku',
  url='https://github.com/Nkyoku/pyvcroid2',
  description='Python Library to Access to Core DLL of VOICEROID2',
  license='MIT',
  packages=find_packages(),
  entry_points={
    'console_scripts': [
      'pyvcroid2 = pyvcroid2.pyvcroid2:script'
    ]
  }
)
