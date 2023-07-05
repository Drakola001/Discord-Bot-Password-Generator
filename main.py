#Discord Bot Password Generator
#Made by drakola001 on discord
#Join our discord https://discord.gg/QVApSTJWP6
#Make sure to read README

import discord
from discord.ext import commands
import random

intents = discord.Intents.all()
Client = commands.Bot(command_prefix="!", intents=intents)


@Client.event
async def on_ready():
    print("Bot is online and ready to use")


class PasswordView(discord.ui.View):
    def __init__(self, password):
        super().__init__()
        self.password = password

    @discord.ui.button(label="Good", style=discord.ButtonStyle.green, emoji="✅")
    async def good_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(content="You clicked Good! ✅", ephemeral=False)

    @discord.ui.button(label="Not Good", style=discord.ButtonStyle.red, emoji="❌")
    async def not_good_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(content="You clicked Not Good! ❌", ephemeral=False)


@Client.command()
async def gen_pass(ctx, length: int = 5):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()"

    string = lower + upper + numbers + symbols
    password = "".join(random.sample(string, length))

    color = random.choice([
        discord.Color.blue(),
        discord.Color.teal(),
        discord.Color.green(),
        discord.Color.purple(),
        discord.Color.orange(),
        discord.Color.red(),
        discord.Color.gold(),
        discord.Color.magenta()
    ])

    embed = discord.Embed(title="Generated Password", color=color)
    embed.add_field(name="Password", value=f"```\n{password}\n```", inline=False)
    embed.set_footer(text="Made by drakola001")

    view = PasswordView(password)

    await ctx.send(embed=embed, view=view)


Client.run("your token here buddy")
