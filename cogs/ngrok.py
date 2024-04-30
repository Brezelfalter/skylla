from discord.ext import commands
import os
import time

class Ngrok(commands.Cog):
    """
    Comands for Ngrok
    """
    def __init__(self, client):
        self.client = client


    @commands.command(brief="")
    async def ngrok(self, ctx, protocol, port):
        os.system(f"ngrok {protocol} {port} > /dev/null &")

        time.sleep(3)

        output = os.popen('curl http://localhost:4040/api/tunnels | jq ".tunnels[0].public_url"').read()
        output = output.replace('"', '')

        await ctx.send(f"Public sting for command `ngrok {protocol} {port}`:\n\n{output}")


    @commands.command(brief="Kills all ngrok sessions.")
    async def killall(self, ctx):
        os.system("killall ngrok")

        await ctx.send("Killed all ngrok sessions.")


async def setup(client):
    await client.add_cog(Ngrok(client))