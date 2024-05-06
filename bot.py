import discord
import requests

# Define the intents
intents = discord.Intents.default()

# Create a Discord client with the intents
client = discord.Client(intents=intents)

# Define predefined responses
responses = {
    "hello": "Hello! How can I assist you?",
    "goodbye": "Goodbye! Have a great day!",
    "help": "Available commands:\n"
            "!hello - Say hello to the bot\n"
            "!goodbye - Bid farewell to the bot\n"
            "!weather [city] - Get the current weather for a specified city\n"
            "!reminder - Set a reminder for tomorrow at 10:00 AM\n"
            "!reservation - Confirm a reservation for Friday at 7:00 PM\n"
            "For other inquiries, feel free to ask!",
    "weather": "The weather today is sunny with a high of 75°F.",
    "reminder": "Your reminder has been set for tomorrow at 10:00 AM.",
    "reservation": "Your reservation has been confirmed for Friday at 7:00 PM."
}

# Define dynamic responses based on user input
def dynamic_response(message):
    # Check if user input contains keywords
    if "problem" in message.content.lower():
        return "I'm sorry to hear that you're experiencing a problem. Can you provide more details?"
    elif "thank you" in message.content.lower():
        return "You're welcome! If you need any further assistance, feel free to ask."
    else:
        return "I'm sorry, I'm not sure how to respond to that. Can you please rephrase your request?"

# Function to get current weather information using OpenWeatherMap API
def get_weather(city):
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial'
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        weather_description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        return f"The weather in {city.title()} is {weather_description} with a temperature of {temperature}°F."
    else:
        return "Sorry, I couldn't retrieve the weather information at the moment. Please try again later."

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Event handler for when a message is received
@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the message content starts with a command prefix
    if message.content.startswith('!'):
        command = message.content[1:].lower()
        
        # Handle different commands
        if command == 'weather':
            city = message.content.split(' ', 1)[1]
            weather_response = get_weather(city)
            await message.channel.send(weather_response)
        else:
            await message.channel.send("Sorry, I don't recognize that command. Type !help for a list of available commands.")
        return
    
    # Check if the message content matches predefined responses
    for keyword, response in responses.items():
        if keyword in message.content.lower():
            await message.channel.send(response)
            return
    
    # If no predefined response matches, provide a dynamic response
    dynamic_response_text = dynamic_response(message)
    await message.channel.send(dynamic_response_text)

# Run the Discord bot with the specified token
client.run('YOUR_DISCORD_BOT_TOKEN')
