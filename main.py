import discord
from discord.ext import commands, tasks
from discord.utils import get

token = "ur discord bot token here"

intents = discord.Intents().all()
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents, help_command=None, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}\n')


@bot.event
async def on_member_update(before, after):
    guild = after.guild
    role = get(guild.roles, name="Bronze")
    
    if role in after.roles:
        if not any(isinstance(activity, discord.CustomActivity) and activity.name == 'discord.gg/followers' for activity in after.activities):
            await after.remove_roles(role)

@bot.command()
async def bronze(ctx):
    print(f'{ctx.author} | {ctx.author.id} -> /bronze')
    member = ctx.author
    
    embed_reminder = discord.Embed(color=0x800080)
    embed_reminder.add_field(name="𝕭𝖑𝖎𝖓𝖌 - Free Bronze!", value="**Make sure `discord.gg/followers` is in your status to claim!** ```Use command again after adding!```")
    embed_reminder.set_image(url="https://media.discordapp.net/attachments/1189254551308615792/1260270243524378674/download.png")
    await ctx.send(embed=embed_reminder)
    
    if any(isinstance(activity, discord.CustomActivity) and activity.name == 'discord.gg/followers' for activity in member.activities):
        guild = ctx.guild
        role = get(guild.roles, name="Bronze")  
        
        if role:
            await member.add_roles(role)
            embed_success = discord.Embed(color=0x800080, description=f"**I have successfully given you <@&1260261766718423151>,** {member.mention}! `Kindly not remove status or you may lose your role.`")
            embed_success.set_author(name=f'{ctx.guild.name} | Bronze', icon_url='https://images-ext-1.discordapp.net/external/oUMQXSTuxzUO1jpuH6697OPcC7RsXkT548wCp1D2n0E/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1068125718522904657/a_8c01188852aca4797e3d9ddba896c61d.gif')
            await ctx.send(embed=embed_success)
    else:
        embed_status_error = discord.Embed(color=0x800080, description="You need to set your status to 'discord.gg/followers'")
        embed_status_error.set_author(name=f'{ctx.guild.name} | Bronze', icon_url='https://images-ext-1.discordapp.net/external/oUMQXSTuxzUO1jpuH6697OPcC7RsXkT548wCp1D2n0E/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1068125718522904657/a_8c01188852aca4797e3d9ddba896c61d.gif')
        await ctx.send(embed=embed_status_error)


bot.run(token)
