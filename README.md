# discord.py-nuke-bot
Nuke bot using discord.py

Go to https://discord.com/developers/applications -> New Application -> Go to Bot tab under new application and create the Bot then reveal token and copy

Download the bot.py and change the userID to your discord user ID and change the token at the bottom to the token copied previously

Invite to your server and use the commands as required, bot is set to only accept commands from your user:
- *say #channel "message to send" = sends message as the bot
- *roles = gets a list of roles with various privileges
- *role <role> = gives yourself the role specified
- *rename "nickname" = renames all server members to nickname specified
- *mute = mutes all server members
- *kick = kicks all server members
- *ban = bans all server members
- *purge = deletes the last 100 messages from current chat
- *wipe = deletes all channels and then creates a new one called "nuked-by-{USERNAME}" so you can continue to issue commands if needed
- *exec = lets you run custom python code from the bot
