from vdk.api.plugin.hook_markers import hookimpl
from vdk.internal.builtin_plugins.run.job_context import JobContext
from vdk.internal.core.config import ConfigurationBuilder
from vdk.internal.plugin.plugin import PluginRegistry
from typing import List


class QueryValidationPlugin:

    @hookimpl(tryfirst=True)
    def vdk_configure(self, config_builder: ConfigurationBuilder) -> None:
        # Declare needed configuration, it will be injected automatically fron file, env variables, etc.
        config_builder.add(
            key="max_query_size",
            default_value=10000,
            description="The maximum query size in bytes allowed to be executed.",
        )
    
    @hookimpl
    def initialize_job(self, context: JobContext) -> None:
        # Now let's get the correctly configured value
        self._max_query_size = context.core_context.configuration.get_value("max_query_size")

    @hookimpl(trylast=True)
    def db_connection_validate_operation(self, operation, parameters):
        parameters_length = 0
        if parameters:
            parameters_length = len("".join(map(str, parameters)))

        if len(operation) + parameters_length > self._max_query_size:
            raise Exception(
                f"Database operation has exceeded the maximum limit of {self._max_query_size} characters."
            )


@hookimpl
def vdk_start(plugin_registry: PluginRegistry, command_line_args: List) -> None:
    """
    Load all plugin classes
    """
    plugin_registry.load_plugin_with_hooks_impl(QueryValidationPlugin())

