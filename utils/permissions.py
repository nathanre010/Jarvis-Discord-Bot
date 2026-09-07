import discord
from discord.ext import commands

def has_admin_permissions(user: discord.Member, guild: discord.Guild) -> bool:
    """Check if user has admin permissions"""
    return user.guild_permissions.administrator or user == guild.owner

def has_moderate_permissions(user: discord.Member) -> bool:
    """Check if user has moderate permissions"""
    return user.guild_permissions.moderate_members or user.guild_permissions.administrator

def has_manage_messages_permissions(user: discord.Member) -> bool:
    """Check if user has manage messages permissions"""
    return user.guild_permissions.manage_messages or user.guild_permissions.administrator
