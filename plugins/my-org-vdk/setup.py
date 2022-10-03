import setuptools

setuptools.setup(
    name="my-org-vdk",
    version="1.0",
    install_requires=[
        "vdk-core",
        "vdk-plugin-control-cli",
        "vdk-postgres",
        "vdk-snowflake",
        "vdk-ingest-http",
        "vdk-ingest-file",
        "vdk-config-prod-plugin",
        "vdk-my-validate"
    ]
)