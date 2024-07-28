import discord
import captcha
import random
import dotenv
import os
from discord.ext import commands
from captcha.image import ImageCaptcha
from dotenv import load_dotenv, dotenv_values

# Load the class with the buttons and embeds
class MyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="Verify", style=discord.ButtonStyle.green, custom_id="verifybutton")
    async def button_callback(self, button, interaction):   
        user = interaction.user
        my_view = MyView()
        role_namever = "verifying"  
        rolemember_ver = discord.utils.get(interaction.guild.roles, name=role_namever)
        embed = discord.Embed(description="Verification Process Step 1/2 - Check DMs", color=discord.Color.orange())
        embed2 = discord.Embed(description="You are already verified.", color=discord.Color.brand_red())
        embed3 = discord.Embed(description="You cannot verify multiple times", color=discord.Color.brand_red())
        if rolemember_ver in user.roles:
            await interaction.response.send_message(embed=embed3, ephemeral=True)
        else:
            await user.add_roles(rolemember_ver)
            await interaction.response.send_message(embed=embed, ephemeral=True)  
            role_namemember = "Member" 
            rolemember = discord.utils.get(interaction.guild.roles, name=role_namemember)
            if rolemember:
                # Generate and load the Captcha
                image = ImageCaptcha(width=280, height=90)
                captcha_text = random.randint(100000, 999999)
                captcha_text = str(captcha_text)
                data = image.generate(captcha_text)
                image.write(captcha_text, "captcha/CAPTCHA.jpg")
                image_path = 'captcha/CAPTCHA.jpg'
                file = discord.File(image_path, filename="CAPTCHA.jpg")

                # Load the embeds
                embed4 = discord.Embed(description="Step 2/2 - Please complete the captcha.", color=discord.Color.orange())
                embed4.set_image(url="attachment://CAPTCHA.jpg")
                embed5 = discord.Embed(description="Step 2/2 Complete. You are verified.", color=discord.Color.brand_green())
                
                # Send the user the embeds
                await user.send(file=file, embed=embed4)
                print(captcha_text)
                while True:
                    msg = await bot.wait_for("message", check=lambda check: check.author.id == user.id)
                    if msg.guild is None:
                        if msg.content == captcha_text:
                            await user.send(embed=embed5)
                            await user.add_roles(rolemember)
                            await user.remove_roles(rolemember_ver)
            else:
                await interaction.response.send_message(embed=embed2, ephemeral=True)  

# Load Dotenv
load_dotenv()

# Load the intents
intents = discord.Intents.all()
bot = commands.Bot(intents=intents)

# Bot Events
@bot.event
async def on_ready():
    # The add_view is meant to make the button persistant (you can restart the bot and the button doesn't expire)
    bot.add_view(MyView())
    print(f'Logged on as {bot.user}!')

# Bot Commands
@bot.slash_command(name="verify")
async def verify(ctx):
    my_view = MyView()
    sender = ctx.author
    role_has = discord.utils.get(ctx.guild.roles, name="Member")

    embed = discord.Embed(description="Click the button below to verify via captcha", color=discord.Color.brand_green())
    await ctx.respond(embed=embed, view=my_view)

# Run the bot
bot.run(os.getenv("TOKEN"))
