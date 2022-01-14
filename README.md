# DiscordBot-Cog-HotReload

A simple script that loads and hot-reloads cogs when you save any changes

# Usage
```py
@bot.event
async def on_ready():
    from HotReloadModules import HotLoad
    await HotLoad(bot)

```
simply import and run the `HotLoad` function, passing in the bot instance. \
It will load any cogs in the `./cogs` folder and watch any changes.
