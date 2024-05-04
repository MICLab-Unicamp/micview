import setuptools
from micview import __version__

with open(file="README.md", mode="r") as fh:
    long_description: str = fh.read()

found: "list[str]" = setuptools.find_packages()

setuptools.setup(
    name="MICView",
    version=__version__,
    author="Caio Ruiz Coldebella",
    author_email="c232621@dac.unicamp.br",
    description="Open-source GUI for visualization of multimodal medical images and segmentations viewing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MICLab-Unicamp/micview/archive/refs/tags/v1.0.0.tar.gz",
    packages=found,
    include_package_data=True,
    package_data={'micview': ["assets/miclab_logo.jpg"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=['setuptools', 'numpy>=1.22', 'pillow>=9.0.0',
    'SimpleITK>=2.3.0', 'screeninfo>=0.8.1', 'pydicom', 'dicom2nifti', 'matplotlib'],
    entry_points={
        'console_scripts': ["micview = micview.run:main"]
    }
)