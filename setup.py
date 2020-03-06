from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='quippy-cli',
      version='0.0.1',
      description='snippet manager for the CLI',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/nk412/quippy',
      author='Nagarjuna Kumarappan',
      author_email='nagarjuna.412@gmail.com',
      license='MIT',
      packages=['quippy-cli'],
      install_requires=[
          'pyfzf>=0.2.1', 'pyperclip>=1.7.0', 'PyYAML>=5.3'
      ],
      entry_points={
        'console_scripts': ['qp=quippy.quippy:main']
      },
      zip_safe=False)
