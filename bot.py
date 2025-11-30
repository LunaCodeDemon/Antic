import os
import hikari
import tanjun
from dotenv import load_dotenv

def main():
    load_dotenv()
    bot = hikari.GatewayBot(os.environ.get("DISCORD_TOKEN"))
    client = tanjun.Client.from_gateway_bot(bot)

    client.load_modules("bot.components.loader")

    bot.run()

if __name__ == "__main__":
    main()
