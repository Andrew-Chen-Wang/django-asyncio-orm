from setuptools import find_packages, setup

long_desc = (
    open("README.md", "rb").read().decode("utf-8")
    + "\n\n"
    + open("CHANGELOG.md", "rb").read().decode("utf-8")
)

setup(
    name="django-asyncio-orm",
    version="0.1.0",
    description="Django native async ORM.",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    author="Andrew Chen Wang",
    author_email="acwangpython@gmail.com",
    license="Apache License 2.0",
    url="http://github.com/Andrew-Chen-Wang/django-asyncio-orm",
    packages=find_packages(),
    install_requires=["django", "aiosqlite"],
    tests_require=["tox"],
    keywords=["django", "async", "async ORM", "ORM", "asyncio", "aiosqlite"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    zip_safe=False,
)
