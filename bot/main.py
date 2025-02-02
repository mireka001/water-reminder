import json
import discord
from discord.ext import commands, tasks
import os
import time



bot = commands.Bot('$')
client = discord.Client()


target_channel_id = 701468290047934536
general_channel_id = 701468290047934536
@client.event
async def on_message(message):
    if message.author == client.user:
        return
#embed(s):
@tasks.loop(seconds = 10)
async def called_every_three_hours():
    message_channel = bot.get_channel(general_channel_id)
    print(f"Got channel {message_channel}")
    await message_channel.send("Don't forget to drink water <3")

#Cron task reminder every 3 hours loop console print
@called_every_three_hours.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")
called_every_three_hours.start()

incorrect_emoji = "<:amsiedad:995873221482139750>"
def evaluate(exp, curr_count):

    # Disregard expressions with letters
    if any(char.isalpha() for char in exp):
        return [float("-inf"), False]
    # Replace exponentiation, multiplication and division signs with Pythonic equivalents
    temp = exp.replace("^", "**").replace("ร—", "*").replace("รท", "/")
    # Perform the calculation
    try:
        result = eval(temp)
    except:
        return [float("-inf"), False]
    # Check if current expression evaluates to 1 more than curr_count
    return [result, result == curr_count + 1]
client = discord.Client()
@client.event
async def on_ready():
    """
    Checks last valid count (due to bot cycling). Confirms that the bot is ready to use.
    """
    global incorrect_emoji
    # List of forbidden start/end characters
    char_arr = ["~", "`", ".", ",", "!", "@", "#", "$", "%", "^", "&", ":", ";", "/", "\\",
                "*", "(", ")", "<", ">", "?", "{", "}", "[", "]", "\"", "'", "|", "_", "="]
    # Access JSON file for updating last count
    filename = os.path.dirname(os.path.realpath(__file__)) + '/data.json'
    with open(filename, "r", encoding="utf-8") as file1:
        data = json.load(file1)
    # Get counting channel history
    c_id = int(os.getenv("CHANNEL_ID"))
    channel_hist = await client.get_channel(c_id).history(limit=float("inf")).flatten()
    # Create flag to avoid checking every message in the channel, only the last valid one
    checked_flag = False
    # Name of last count and last counter
    result_g = 0
    last_counter = "None"
    for msg in channel_hist:
        # Stop checking if last valid message has been checked
        if checked_flag:
            break
        split_arr = msg.content.split()
        if len(split_arr) != 0:
            expression = split_arr[0]
            result = evaluate(expression, data["curr_count"])[0]
            # If expression can be evaluated
            # If expression starts or ends with forbidden character
            evaluateable = result != float("-inf")
            with_fb = any(expression.startswith(fb_char) for fb_char in char_arr) or any(
                expression.endswith(fb_char) for fb_char in char_arr)
            # Message neither starts nor ends with forbidden character
            # If expression can be evaluated
            if evaluateable and (not with_fb):
                react_arr = msg.reactions
                for emo1 in react_arr:
                    # Only care about emoji sent by bot for checked flag
                    if emo1.me:
                        checked_flag = True
                        # Store 0 as last count if "incorrect" emoji is used, store result otherwise
                        if incorrect_emoji[-19:-1] == str(emo1.emoji.id):
                            data["curr_count"] = 0
                            data["last_user"] = 0
                        else:
                            data["curr_count"] = result
                            data["last_user"] = msg.author.id
                            result_g = result
                            last_counter = msg.author.name
                        break
    print(f"{result_g} by {last_counter}")
    # Update JSON file
    with open(filename, "w", encoding="utf-8") as file2:
        json.dump(data, file2, indent=4)
  # Change bot status
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="if you're drinking water"))
    return


@client.event
async def on_message(message):
    
    if message.author == bot.user:
        return
    if message.content.lower().strip().startswith('$agua'):
        await message.channel.send('Tomen aguita cabros <3')
        time.sleep(2)
        await message.delete() 
        

        
        
    global incorrect_emoji
    
    # Don't check message if written by self
    if message.author == client.user:
        return
    # Access JSON file for counting checked and verified sentences
    filename = os.path.dirname(os.path.realpath(__file__)) + '/data.json'
    with open(filename, "r", encoding="utf-8") as file1:
        data = json.load(file1)
    # Only react to other messages if they are sent in counting channel
    if message.channel.id == int(os.getenv("CHANNEL_ID")):
        # List of possible reactions
        emoji_list = [incorrect_emoji,                                          # 0, incorrect
                      "<:mamadissimo:995872944326713344>",                         # 1, correct
                      "<:noice:995873451736825926>",                          # 2, 69
                      "<:9340dippyshrug:901635891045466193>",                         # 3, every 10 under 100
                      "<:9340dippyshrug:901635891045466193>"                       # 4, every 100 under 1000
                      ]
        # List of forbidden start/end characters
        char_arr = ["~", "`", ".", ",", "!", "@", "#", "$", "%", "^", "&", ":", ";", "/", "\\",
                    "*", "(", ")", "<", ">", "?", "{", "}", "[", "]", "\"", "'", "|", "_", "="]
        # See stats using tailwhip!user <@user>; user parameter is optional
        if message.content.startswith('!countstats'):
            # Determine whose stats to analyse
            u_id = ""
            msg_arr = message.content.split()
            if len(msg_arr) == 1:
                u_id = str(message.author.id)
            elif msg_arr[1][:2] == "<@":
                u_id = msg_arr[1][3:21]
            else:
                return
            # Initialise counting stats
            count_total = 0
            count_correct = 0
            # Read entire channel history
            channel_hist = await message.channel.history(limit=float("inf")).flatten()
            for msg in channel_hist:
                split_arr = msg.content.split()
                if len(split_arr) != 0:
                    expression = split_arr[0]
                    # If expression can be evaluated
                    # If expression starts with forbidden character
                    # If message is written by user in question
                    evaluateable = evaluate(expression, data["curr_count"])[
                        0] != float("-inf")
                    with_fb = any(msg.content.startswith(fb_char) for fb_char in char_arr) or any(
                        msg.content.endswith(fb_char) for fb_char in char_arr)
                    author_verif = str(msg.author.id) == u_id
                    # Message does not start with forbidden character
                    # If expression can be evaluated and written by user in question
                    if evaluateable and (not with_fb) and author_verif:
                        react_arr = msg.reactions
                        for emo1 in react_arr:
                            # Only care about emoji sent by bot for total count
                            if emo1.me:
                                count_total += 1
                                # Increment correct count if "incorrect" emoji NOT used
                                if emoji_list[0][-19:-1] != str(emo1.emoji.id):
                                    count_correct += 1
            ct_str = f"โ€ข Total counts from <@{u_id}>: {count_total}"
            cc_str = f"โ€ข Correct counts from <@{u_id}>: {count_correct}"
            sc_str = "have fun"
            embed_m = discord.Embed()
            # Special case: user has never counted (avoiding ZeroDivisionError)
            if count_total == 0:
                ca_str_0 = f"โ€ข Counting accuracy of <@{u_id}>: ๐—ก/๐—”"
                stats_arr = [ct_str, cc_str, ca_str_0, sc_str]
            else:
                ca_str = f"โ€ข Counting accuracy of <@{u_id}>: {round(count_correct / count_total * 100, 5)}%"
                stats_arr = [ct_str, cc_str, ca_str]
            embed_m.add_field(
                name="Counting stats",
                value="\n".join(stats_arr))
            await message.channel.send(embed=embed_m)
        else:
            msg_arr = message.content.split()
            if len(msg_arr) == 0:
                return
            # Evaluate first string before whitespace
            expression = message.content.split()[0]
            # If expression starts with forbidden character
            with_fb = any(expression.startswith(fb_char) for fb_char in char_arr) or any(
                expression.endswith(fb_char) for fb_char in char_arr)
            # Disregard if there are letters
            if (not any(char.isalpha() for char in expression)) and (not with_fb) and ("@" not in expression):
                # Check using evaluate and check for user repeat counting
                result = evaluate(expression, data["curr_count"])
                if result[1] and data["last_user"] != message.author.id:
                    data["last_user"] = message.author.id
                    data["curr_count"] = result[0]
                    emoji = emoji_list[1]
                    # Select appropriate emoji
                    if data["curr_count"] == 69:
                        emoji = emoji_list[2]
                    elif data["curr_count"] % 10 == 0 and data["curr_count"] < 100:
                        emoji = emoji_list[3]
                    elif data["curr_count"] % 100 == 0 and data["curr_count"] <= 1000:
                        emoji = emoji_list[4]
                    await message.add_reaction(emoji)
                else:
                    # Send "incorrect" emoji
                    await message.add_reaction(emoji_list[0])
                    # Reset all data except for counting channel
                    data["curr_count"] = 0
                    data["last_user"] = 0

                    embed_m = discord.Embed(
                        colour=0x2347c0, title="`Wrong Count`")
                    embed_m.set_image(
                        url="https://www.hdnicewallpapers.com/Walls/Normal/Love%20Heart/Awesome_Love_Heart_Sign_in_Water_HD_Wallpapers.jpg")
                    await message.channel.send(embed=embed_m)

     # Update JSON file
    with open(filename, "w", encoding="utf-8") as file2:
        json.dump(data, file2, indent=4)
    return
   
client.run(os.getenv("DISCORD_TOKEN"))
