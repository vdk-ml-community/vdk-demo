import setuptools

setuptools.setup(
    name="vdk-my-validation",
    version="1.0",
    packages=setuptools.find_namespace_packages(),
    entry_points={
        "vdk.plugin.run": [
            "vdk-my-validation-plugin = vdk_my_validation",
        ]
    }
)
