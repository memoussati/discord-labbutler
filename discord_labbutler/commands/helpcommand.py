from discord_labbutler import commands
from discord_labbutler.command import Command, CommandException, CommandMessage


class HelpCommand(Command):
    """
    **Shows help information on LabBot commands.**
`help <command>  --  Displays help for a specific command.`"""

    def run(self, ctx, args):
        cmd = args

        # No argument given
        if cmd is None:
            command_list = '\n\n**Available commands**\n```'
            for c in commands.IDENTIFIERS:
                command_list += "\n *  {}".format(c)
            command_list += '```'

            return CommandMessage(content=self.__doc__ + command_list)
        # Not in command list
        elif cmd not in commands.IDENTIFIERS:
            raise CommandException('Command "{}" was not found.'.format(cmd))

        return CommandMessage(content=commands.IDENTIFIERS[cmd].__doc__)
