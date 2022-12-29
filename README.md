# ChatGPT-Discord-bot

This is Discord bot which connecting to ChatGPT via OpenAPI

# Prerequisites
You nees to have:
1. Pyhton 3+
2. pip
3. discord and openai librarys

# Installing
1. Create a Discord account and join a server where you have permission to create a bot.
2. Go to the Discord Developer Portal (https://discord.com/developers/applications) and log in with your Discord account.
3. Click on the "New Application" button. Give your application a name, and click the "Create" button.
4. On the next page, click on the "Create a Bot" button.
5. Click on the "Copy" button next to the "Token" field to copy your bot's token to your clipboard. You will use this token to authenticate your bot when you set it up.
6. Install the Discord.py library using pip:
`pip install discord.py`
7. Install the openai Python library using pip:
`pip install openai`
8. Sign up for an API key for the ChatGPT API at the OpenAI website (https://beta.openai.com/signup/).
9. Replace YOUR_API_KEY_HERE in the code with your actual ChatGPT API key, and replace YOUR_BOT_TOKEN_HERE with your actual bot token.

# Launch
1. To add a bot to a Discord server, you will need to have the "Manage Server" permissions on the server. Here is the process for adding a bot to a Discord server:
2. Go to the Discord Developer Portal (https://discord.com/developers/applications) and log in with your Discord account.
3. Click on the application that represents your bot.
4. Click on the "Generate Invite" button.
5. Select the server you want to add the bot to from the "Server" dropdown menu.
6. Select the permissions that you want the bot to have. You can choose to grant the bot access to specific channels, or you can give it full permissions to the server.
7. Click on the "Generate Link" button.
8. Follow the link to invite the bot to the server. You may need to log in to your Discord account again to complete the process.
9. Once the bot has been added to the server, you can use the !invite command in Discord to get the invite link for the bot.
10. Share the invite link with anyone you want to be able to invite the bot to their own server.
11. Run the Python script to start the bot.
`python bot.py`

# Commands
To have the bot generate a response using the ChatGPT API, you can use the !response command. 
For example, you could type "!response What is the weather like today?" to have the bot generate a response to your question.

You can find more information in the Discord API documentation (https://discord.com/developers/docs/intro) and the Discord.py documentation (https://discordpy.readthedocs.io/).
