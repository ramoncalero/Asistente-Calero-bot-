import os
import discord
from discord import app_commands

# Token desde Render
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Intents necesarios
intents = discord.Intents.default()
intents.message_content = False  # No lo necesitamos para comandos slash

class AsistenteCalero(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Registrar / sincronizar comandos con Discord
        await self.tree.sync()
        print("✅ Comandos / sincronizados correctamente.")

    async def on_ready(self):
        print(f"🤖 Bot conectado como: {self.user}")

bot = AsistenteCalero()

# ------- COMANDO /hola -------
@bot.tree.command(name="hola", description="El bot te saluda.")
async def hola(interaccion: discord.Interaction):
    await interaccion.response.send_message("👋 ¡Hola! Soy el asistente del servidor.", ephemeral=False)

# ---------------------------------

# Comienza la ejecución
if not DISCORD_TOKEN:
    raise RuntimeError("❌ Falta la variable DISCORD_TOKEN en Render.")

bot.run(DISCORD_TOKEN)
