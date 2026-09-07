import discord
from discord.ext import commands
from discord import app_commands
from config import COLOR_ERROR, COLOR_SUCCESS, COLOR_WARNING

class Security(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.db
    
    @app_commands.command(name="verify", description="Système de vérification pour le serveur")
    async def verify(self, interaction: discord.Interaction):
        """Verify member on server"""
        
        embed = discord.Embed(
            title="✅ Vérification",
            description="Vous avez été vérifié avec succès!",
            color=COLOR_SUCCESS
        )
        
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Security(bot))
