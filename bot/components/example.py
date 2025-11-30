import tanjun

component = tanjun.Component()

@component.with_slash_command
@tanjun.as_slash_command("hello", "Say hello!")
async def hello_command(ctx: tanjun.abc.Context) -> None:
    await ctx.respond("Hello, world!")

@tanjun.as_loader
def load_component(client: tanjun.Client) -> None:
    client.add_component(component.copy())
