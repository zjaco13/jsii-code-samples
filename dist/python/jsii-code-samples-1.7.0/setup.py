import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "jsii-code-samples",
    "version": "1.7.0",
    "description": "Code samples that accompany the AWS blog post on jsii",
    "license": "MIT-0",
    "url": "https://github.com/zjaco13/jsii-code-samples#readme",
    "long_description_content_type": "text/markdown",
    "author": "Zach Jacobson <zjacobso@amazon.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/zjaco13/jsii-code-samples.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "jsii_code_samples",
        "jsii_code_samples._jsii"
    ],
    "package_data": {
        "jsii_code_samples._jsii": [
            "jsii-code-samples@1.7.0.jsii.tgz"
        ],
        "jsii_code_samples": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "jsii>=1.84.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
