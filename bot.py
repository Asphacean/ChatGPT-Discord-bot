import logging
import discord
import openai

# Replace YOUR_API_KEY_HERE with your actual API key
openai.api_key = "YOUR_OPEN_API_TOKEN"

# Set up logging
logging.basicConfig(level=logging.INFO)

client = discord.Client(
    intents=discord.Intents().all()
)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!response"):
        # Extract the command arguments
        prompt = message.content[9:]
        # Generate a response using the ChatGPT API
        response = openai.Completion.create(
            prompt=prompt,
            model="text-davinci-002"
        )
        # Check if the response object has a 'choices' attribute
        if hasattr(response, "choices"):
            # Get the first choice from the 'choices' list
            choice = response.choices[0]
            # Get the response text from the 'text' attribute
            response_text = choice.text
            # Send the response to the Discord channel
            await message.channel.send(response_text)
            # Log the response
            logging.info(f"Generated response for prompt '{prompt}': {response_text}")
        else:
            # Handle the error
            await message.channel.send("An error occurred while generating the response.")
            # Log the error
            logging.error("Failed to generate response: response object does not have a 'choices' attribute.")

# Replace YOUR_BOT_TOKEN_HERE with your actual bot token
client.run("YOUR_DISCORD_BOT_TOKEN")
