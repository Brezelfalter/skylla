from discord.ext import commands
from pyngrok import ngrok


class Ngrok(commands.Cog):
    """
    Comands for Ngrok
    """
    def __init__(self, client):
        self.client = client
    

    @commands.command(brief="Create ngrok connection URL.")
    async def ngrok(self, ctx, port:str, protocol:str):
        connection = ngrok.connect(port, protocol).public_url
        
        await ctx.send(f"NGROK URL:\n`{connection}`")


    @commands.command(brief="Kill ngrok processes.")
    async def kill(self, ctx):
        ngrok.kill()

        await ctx.send("Killed ngrok processes.")


async def setup(client):
    await client.add_cog(Ngrok(client))