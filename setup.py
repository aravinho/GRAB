from setuptools import setup


setup(
    name='GRAB',
    include_package_data=True,
    description='Making GRAB repo into a pip package',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    version='0.1',
    url='https://github.com/aravinho/GRAB',
    author='Omid Taheri',
    author_email='omid.taheri@tuebingen.mpg.de',
    maintainer='Aravind Sivakumar',
    maintainer_email='aravinho@gmail.com',
    install_requires=[
          'numpy>=1.16.2',
          'pillow',
          'pyrender>=0.1.23',
          'PyYAML',
          'smplx>=0.1.2',
          'torch>=1.0.1.post2',
          'torchgeometry>=0.1.2',
          'tqdm',
          'trimesh'
      ],
      packages=['grab']

    )

