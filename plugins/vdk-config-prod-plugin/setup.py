import setuptools

setuptools.setup(
    name="vdk-config-prod-plugin",
    version="1.0",
    packages=setuptools.find_namespace_packages(),
    entry_points={
        "vdk.plugin.run": [
            "my-config-prod-plugin = my_prod_config",
        ]
    }
)
