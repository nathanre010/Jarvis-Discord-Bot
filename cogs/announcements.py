import discord
from discord.ext import commands
from discord import app_commands
from config import COLOR_ERROR, COLOR_SUCCESS, COLOR_INFO, BOT_OWNER_ID

class Announcements(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.db
    
    @app_commands.command(name="annonce-bot", description="Faire une annonce dans un salon")
    @app_commands.describe(salon="Le salon où faire l'annonce", message="Le message d'annonce")
    async def annonce_bot(self, interaction: discord.Interaction, salon: discord.TextChannel, message: str):
        """Make an announcement in a channel"""
        
        if not interaction.user.guild_permissions.administrator and interaction.user.id != interaction.guild.owner_id:
            embed = discord.Embed(
                title="❌ Permission Refusée",
                description="Vous devez être administrateur pour faire une annonce.",
                color=COLOR_ERROR
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        try:
            embed = discord.Embed(
                title="📢 Annonce",
                description=message,
                color=COLOR_INFO
            )
            embed.set_footer(text=f"Annoncé par {interaction.user.name}")
            
            await salon.send(embed=embed)
            
            embed_success = discord.Embed(
                title="✅ Annonce Envoyée",
                description=f"Annonce envoyée dans {salon.mention}",
                color=COLOR_SUCCESS
            )
            
            await interaction.response.send_message(embed=embed_success)
        except Exception as e:
            embed = discord.Embed(
                title="❌ Erreur",
                description=f"Impossible d'envoyer l'annonce: {str(e)}",
                color=COLOR_ERROR
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Announcements(bot))
