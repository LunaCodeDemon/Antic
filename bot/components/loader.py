import tanjun

@tanjun.as_loader
def load_components(client: tanjun.Client) -> None:
    client.load_modules("bot.components.example")
