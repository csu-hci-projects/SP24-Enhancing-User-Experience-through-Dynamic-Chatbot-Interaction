# SP24-BotSpeak: Enhancing User Experience through Dynamic Chatbot Interaction

Discord Chatbot
Description
This is a simple Discord chatbot written in Python using the discord.py library. The chatbot responds to user messages with predefined responses and can fetch current weather information for a specified city using the OpenWeatherMap API.

Prerequisites
Before running the chatbot program, you'll need the following prerequisites:

Python 3 installed on your system
Discord account
Discord bot token
OpenWeatherMap API key
Setup
Clone or download the repository to your local machine.
Install the required Python packages using conda install conda-forge::discord.py

Configuration
Obtain a Discord bot token by creating a new bot application on the Discord Developer Portal: https://discord.com/developers/applications
Obtain an OpenWeatherMap API key by signing up for an account on the OpenWeatherMap website: https://home.openweathermap.org/users/sign_up
Replace YOUR_DISCORD_BOT_TOKEN with your Discord bot token in the bot.py file.
Replace YOUR_OPENWEATHERMAP_API_KEY with your OpenWeatherMap API key in the bot.py file.

Usage
Run the bot program by executing the following command in your terminal: python bot.py
Once the bot is running, it will log in to Discord and be ready to respond to messages in the specified server.
To interact with the bot, simply type messages in any channel where the bot is present.
Predefined responses:
Typing hello will trigger a greeting response from the bot.
Typing help will prompt the bot to offer assistance.
Typing weather [city] (e.g., weather New York) will fetch current weather information for the specified city.
Typing reminder will confirm the setting of a reminder for the user.
Typing reservation will confirm the booking of a reservation for the user.
To use the !weather command, type !weather [city] in any channel where the bot is present.
When messaging the bot make sure to @[botname] ![command] fill in with the appropriate name and command.

Additional Notes
This is a simple demonstration of a Discord chatbot and can be further customized and extended to meet specific requirements.
Make sure to keep your Discord bot token and OpenWeatherMap API key secure and do not share them publicly.

The weather command is the difficulty spike and frustration with the chatbot

You will have to create a discord bot token as using mine will reset the token and break the bot!
