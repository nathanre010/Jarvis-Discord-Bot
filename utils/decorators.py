import discord
from discord.ext import commands
from functools import wraps
from config import BOT_OWNER_ID, COLOR_ERROR

def owner_only():
    """Decorator to check if user is bot owner"""
    def decorator(func):
        @wraps(func)
        async def wrapper(self, interaction: discord.Interaction, *args, **kwargs):
            if interaction.user.id != BOT_OWNER_ID:
                embed = discord.Embed(
                    title="❌ Permission Refusée",
                    description="Seul le propriétaire du bot peut utiliser cette commande.",
                    color=COLOR_ERROR
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)
                return
            return await func(self, interaction, *args, **kwargs)
        return wrapper
    return decorator
