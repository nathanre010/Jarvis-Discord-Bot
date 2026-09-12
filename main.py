"""
Jarvis - Discord Bot
Bot Discord complet avec système de modération, configuration, commandes et sécurité avancée
"""

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration du bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Événement: Bot prêt
@bot.event
async def on_ready():
    print(f"✅ {bot.user} est connecté et prêt!")
    print(f"ID du bot: {bot.user.id}")
    
    # Définir le statut du bot
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="🔒 Jarvis Moderation"
        )
    )

# Événement: Erreur de commande
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ Commande non trouvée. Utilise `!help` pour voir les commandes disponibles.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"❌ Arguments manquants: {error}")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Vous n'avez pas les permissions nécessaires pour cette commande.")
    else:
        await ctx.send(f"❌ Une erreur s'est produite: {error}")

# Charger les cogs (extensions)
async def load_cogs():
    """Charge tous les cogs du dossier cogs"""
    cogs_dir = "cogs"
    if os.path.exists(cogs_dir):
        for filename in os.listdir(cogs_dir):
            if filename.endswith(".py"):
                try:
                    await bot.load_extension(f"cogs.{filename[:-3]}")
                    print(f"✅ Cog chargé: {filename}")
                except Exception as e:
                    print(f"❌ Erreur en chargeant {filename}: {e}")
    else:
        print(f"⚠️  Dossier '{cogs_dir}' non trouvé")

# Fonction principale
async def main():
    """Démarre le bot"""
    async with bot:
        await load_cogs()
        token = os.getenv("DISCORD_TOKEN")
        if not token:
            print("❌ Erreur: DISCORD_TOKEN non trouvé dans le fichier .env")
            return
        await bot.start(token)

# Lancer le bot
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
