from discord_labbutler.command import Command, CommandException, CommandMessage


class TestCommand(Command):
    """**Runs a test command.**"""

    def run(self, ctx, args):
        return CommandMessage(content="""{} wants to test something.
arguments: `{}`""".format(ctx.author.mention, args))
