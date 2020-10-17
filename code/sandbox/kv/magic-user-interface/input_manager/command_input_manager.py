import click


@click.group(invoke_without_command=True)
def init_all_commands():
    pass


@init_all_commands.command()
def file():
    pass


@init_all_commands.command()
def folder():
    pass


@init_all_commands.command()
def directory():
    pass


@init_all_commands.command()
def software():
    pass


@init_all_commands.command()
def ip():
    pass


@init_all_commands.command()
def ping():
    pass


@init_all_commands.command()
def process():
    pass


@init_all_commands.command()
def system():
    pass


@init_all_commands.command()
def disk():
    pass


@init_all_commands.command()
def terminal():
    pass



