import setuptools
from src import __version__

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
    url="https://github.com/MICLab-Unicamp/micview.git",
    packages=found,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    python_requires='>=3.8',
    install_requires=['setuptools', 'numpy>=1.22', 'scipy>=1.6.0', 'pillow>=9.0.0', 'SimpleITK>=2.3.0', 'screeninfo>=0.8.1'],
    entry_points={
        'console_scripts': ["micview = src.micview.run:main"]
    }
)