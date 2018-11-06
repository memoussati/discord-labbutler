#!/usr/bin/env python3
"""
Phil's LabBot for Discord.

An extensible Discord chatbot with a low profile.
"""
import logging
import discord
from discord_labbutler import config, commands
from discord_labbutler.command import CommandException

# Logging
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s/%(levelname)s](%(name)-12s) %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger('discord_labbutler')

# Discord client setup
client = discord.Client()


@client.event
async def on_message(ctx):
    """Triggered for each new message on any available channel."""
    # Do not trigger on messages of this bot
    if ctx.author == client.user:
        return

    # Only do something if message starts with the magic prefix
    if ctx.content.startswith(config.PREFIX + ' '):
        parts = config.SPLIT.split(ctx.content)
        command = parts[1] if len(parts) > 1 else None
        args = ' '.join(parts[2:]) if len(parts) > 2 else None

        # A valid command is required
        if command is None or command not in commands.IDENTIFIERS:
            return
        else:
            logger.info('user "{}" executed: {}'.format(
                ctx.author, ctx.content))

        # Send normal message
        try:
            msg = commands.IDENTIFIERS[command]().run(ctx=ctx, args=args)
            await client.send_message(ctx.channel,
                                      content=msg.content,
                                      embed=msg.embed)

        # Error message with embed style
        except CommandException as e:
            msg = discord.Embed(title="I cannot do that!",
                                description=str(e), color=0xff0000)
            await client.send_message(ctx.channel, embed=msg)

        # Blame the programmer
        except Exception as e:
            logger.warn('Unhandled command error: {}: {} {} ==> {}'.format(
                ctx.author, command, args, e))


@client.event
async def on_ready():
    """Triggered when a successful connection has been established."""
    logger.info('LabBot ready!')
    logger.info('logged in as "{}" with ID #{}'.format(
        client.user.name, client.user.id))


# Run the bot
try:
    client.run(config.TOKEN)
except Exception as e:
    logger.error('Error while connecting to Discord: {}'.format(e))
