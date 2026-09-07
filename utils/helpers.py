import discord
from discord.ext import commands
from config import COLOR_ERROR, COLOR_SUCCESS, COLOR_INFO, COLOR_WARNING

def create_error_embed(title: str, description: str):
    """Create an error embed"""
    return discord.Embed(
        title=title,
        description=description,
        color=COLOR_ERROR
    )

def create_success_embed(title: str, description: str):
    """Create a success embed"""
    return discord.Embed(
        title=title,
        description=description,
        color=COLOR_SUCCESS
    )

def create_info_embed(title: str, description: str):
    """Create an info embed"""
    return discord.Embed(
        title=title,
        description=description,
        color=COLOR_INFO
    )

def create_warning_embed(title: str, description: str):
    """Create a warning embed"""
    return discord.Embed(
        title=title,
        description=description,
        color=COLOR_WARNING
    )
