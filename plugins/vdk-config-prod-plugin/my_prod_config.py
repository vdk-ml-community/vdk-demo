from vdk.api.plugin.hook_markers import hookimpl
from vdk.internal.core.config import ConfigurationBuilder


@hookimpl
def vdk_configure(config_builder: ConfigurationBuilder):
    # Ingestion
    config_builder.set_value(key="INGEST_METHOD_DEFAULT", value="POSTGRES")

    # Postgres
    config_builder.set_value(key="POSTGRES_HOST", value="sql.postgres.com")
    config_builder.set_value(key="POSTGRES_PORT", value=25034)
    config_builder.set_value(key="POSTGRES_USE_SSL", value=True)
    config_builder.set_value(key="POSTGRES_AUTH_MECHANISM", value="GSSAPI")
    config_builder.set_value(key="POSTGRES_USER", value=None)
    config_builder.set_value(key="POSTGRES_PASSWORD", value=None)
    config_builder.set_value(key="POSTGRES_QUERY_POOL", value="root.data-jobs")
    config_builder.set_value(key="POSTGRES_TIMEOUT", value=3000)
