import click

from ch_tools.common.result import Result
from ch_tools.monrun_checks.clickhouse_client import ClickhouseClient


@click.command("ro-replica")
@click.pass_context
def ro_replica_command(ctx):
    """
    Check for readonly replicated tables.
    """
    ch_client = ClickhouseClient(ctx)

    response = ch_client.execute(
        "SELECT database, table FROM system.replicas WHERE is_readonly"
    )
    if response:
        return Result(2, f"Readonly replica tables: {response}")

    return Result(0, "OK")
