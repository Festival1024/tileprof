from setuptools import setup, find_packages

setup(
    name="protile",
    version="0.1.0",
    description="GPU Kernel Performance Profiler",
    author="Yang Rongjie",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "tilelang>=0.1.7.post3",
    ],
    python_requires=">=3.8",
)