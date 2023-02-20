import disnake
from disnake.ext.commands import when_mentioned_or
from loguru import logger

from tyrant import bot, constants
from tyrant.utils.exceptions import MissingToken

# Set the required Intents to True
intents = disnake.Intents.default()
intents.members = True
intents.message_content = True

# Initialize the bot
bot = bot.Tyrant(
    command_prefix=when_mentioned_or(constants.Bot.prefix),  # Invoked commands must have this prefix
    activity=disnake.Game(name="with fire"),
    case_insensitive=True,
    max_messages=10_000,
    allowed_mentions=disnake.AllowedMentions(everyone=False),
    intents=intents,
)

# Load the extensions we want
bot.load_extension("tyrant.cogs.ask_tyrant")
bot.load_extension("tyrant.cogs.lemon_facts")
bot.load_extension("tyrant.cogs.fruit_vs_vegetables")
bot.load_extension("tyrant.cogs.purge")
bot.load_extension("tyrant.cogs.teamcount")

# Validate the token
token = constants.Bot.token

if token is None:
    raise MissingToken("No token found in the LEMONSAURUS_DISCORD_TOKEN environment variable!")

# Start the bot
logger.info("🍋🍋 Tyrant operational 🍋🍋")
bot.run(token)
