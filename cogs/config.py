import discord
from discord.ext import commands
from discord import app_commands
from config import COLOR_ERROR, COLOR_SUCCESS, COLOR_INFO, BOT_OWNER_ID

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.db
    
    @app_commands.command(name="config", description="Afficher la configuration du serveur")
    async def config(self, interaction: discord.Interaction):
        """Show server configuration"""
        
        if not interaction.user.guild_permissions.administrator and interaction.user.id != interaction.guild.owner_id:
            embed = discord.Embed(
                title="❌ Permission Refusée",
                description="Vous devez être administrateur pour accéder à la configuration.",
                color=COLOR_ERROR
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        embed = discord.Embed(
            title="⚙️ Configuration du Serveur",
            description=f"**Serveur:** {interaction.guild.name}\n**ID:** {interaction.guild.id}\n**Propriétaire:** {interaction.guild.owner.mention}",
            color=COLOR_INFO
        )
        
        embed.add_field(
            name="📊 Statistiques",
            value=f"**Membres:** {interaction.guild.member_count}\n**Rôles:** {len(interaction.guild.roles)}\n**Salons:** {len(interaction.guild.channels)}",
            inline=False
        )
        
        embed.set_thumbnail(url=interaction.guild.icon.url if interaction.guild.icon else None)
        
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Config(bot))
