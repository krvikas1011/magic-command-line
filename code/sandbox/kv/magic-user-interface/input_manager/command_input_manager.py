import click


@click.group(invoke_without_command=True)
def init_all_commands():
    pass


@init_all_commands.command()
def command_1():
    click.echo("Printing 1")
    pass


@init_all_commands.command()
def command_2():
    click.echo("Printing 2")
    pass



