# Phil's Discord Bot
`Not compatible with Python 3.7 yet!`

### Debugging with Visual Studio Code
A launch profile is included in the project which runs the application as
Python Module. To authenticate the bot with Discord, please create a file
named `.env` in the project root and write the following to it:
```bash
BOT_TOKEN="<your-discord-bot-token>"
```

### Running with docker
First, build the docker image:
```
docker build . -t "philslab/discord-labbutler"
```

Then, to execute the container (interactively, for testing!) and set the discord bot token:
```
docker run --rm -it -e "BOT_TOKEN=<your-discord-bot-token>" philslab/discord-labbutler
```
