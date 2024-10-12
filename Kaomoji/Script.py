import json

# A list of kaomojis with their descriptions
kaomojis = [
    {"face": "( ͡° ͜ʖ ͡°)", "name": "Lenny Face"},
    {"face": "¯\\_(ツ)_/¯", "name": "Shrug"},
    {"face": "(╯°□°）╯︵ ┻━┻", "name": "Table Flip"},
    {"face": "(•_•)", "name": "Cool Guy"},
    {"face": "٩(◕‿◕｡)۶", "name": "Happy Dance"},
    {"face": "(ಥ﹏ಥ)", "name": "Crying"},
    {"face": "(¬_¬)", "name": "Suspicious"},
    {"face": "ʕ•ᴥ•ʔ", "name": "Bear"},
    {"face": "(ง'̀-'́)ง", "name": "Fight"},
    {"face": "(∩^o^)⊃━☆ﾟ.*", "name": "Magic"},
    {"face": "(´・ω・｀)", "name": "Sad"},
    {"face": "(づ｡◕‿‿◕｡)づ", "name": "Hug"},
    {"face": "(ง •̀_•́)ง", "name": "Strong"},
    {"face": "(¬‿¬)", "name": "Smirk"},
    {"face": "（＾_＾）", "name": "Smiling"},
    {"face": "｡◕‿◕｡", "name": "Cute"},
    {"face": "(✿◠‿◠)", "name": "Flower"},
    {"face": "(︶︹︺)", "name": "Annoyed"},
    {"face": "(¬_¬”)", "name": "Worried"},
    {"face": "(・`ω´・)", "name": "Determined"},
    {"face": "ヽ(ﾟДﾟ)ﾉ", "name": "Shocked"},
    {"face": "⊂(◉‿◉)つ", "name": "Grabby Hands"},
    {"face": "(☞ﾟヮﾟ)☞", "name": "Cool Point"},
    {"face": "( ͡ಠ ʖ̯ ͡ಠ)", "name": "Disappointed"},
    {"face": "(ง°ل͜°)ง", "name": "Come at me"},
    {"face": "(ಠ_ಠ)", "name": "Disapproval"},
    {"face": "(✧ω✧)", "name": "Excited"},
    {"face": "(•̀ᴗ•́)و", "name": "Winning"},
    {"face": "(T_T)", "name": "Tears"},
    {"face": "(^_^)", "name": "Happy"},
    {"face": "(>_<)", "name": "Struggling"},
    {"face": "(⊙_⊙)", "name": "Surprised"},
    {"face": "ಠ_ಠ", "name": "Skeptical"},
    {"face": "ヽ(￣д￣;)ノ", "name": "Exasperated"},
    {"face": "(ノಠ益ಠ)ノ彡┻━┻", "name": "Angry Table Flip"},
    {"face": "(=^ェ^=)", "name": "Cat"},
    {"face": "(✿´‿`)", "name": "Content"},
    {"face": "(o´▽`o)", "name": "Grinning"},
    {"face": "(´∀｀•)", "name": "Blushing"},
    {"face": "⊙ω⊙", "name": "Big Eyes"},
    {"face": "(ʘ‿ʘ)", "name": "Intrigued"},
    {"face": "(*´Д｀)", "name": "Embarrassed"},
    {"face": "(´･ω･`)", "name": "Meh"},
    {"face": "( ˘︹˘ )", "name": "Displeased"},
    {"face": "(ﾟДﾟ)", "name": "Shocked"},
    {"face": "(─‿‿─)", "name": "Sly"},
    {"face": "( ´ ▽ ` )ﾉ", "name": "Wave"},
    {"face": "(=^･ｪ･^=)", "name": "Happy Cat"},
    {"face": "(´・＿・)", "name": "Gloomy"},
    {"face": "(ʘᗩʘ’)", "name": "Surprised Again"},
    {"face": "ಥ_ಥ", "name": "Tears of Joy"},
    {"face": "(＾◡＾)", "name": "Satisfied"},
    {"face": "☆*:.｡.o(≧▽≦)o.｡.:*☆", "name": "Starry"},
    {"face": "(☉_☉)", "name": "Shocked"},
    {"face": "(｡♥‿♥｡)", "name": "Love"},
    {"face": "(✿◕ ‿◕ฺ)", "name": "Warm Smile"},
    {"face": "(╬ ಠ益ಠ)", "name": "Enraged"},
    {"face": "ᕙ(⇀‸↼‶)ᕗ", "name": "Flexing"},
    {"face": "(☞ﾟヮﾟ)☞", "name": "You"},
    {"face": "(≧◡≦)", "name": "Happy Again"},
    {"face": "(°ロ°)☝", "name": "Idea"},
    {"face": "(•̀o•́)ง", "name": "Pump"},
    {"face": "(O_O;)", "name": "Worried"},
    {"face": "( ´△｀)", "name": "Sigh"},
    {"face": "(ó﹏ò｡)", "name": "Sad Cry"},
    {"face": "ლ(ಠ益ಠლ)", "name": "Rage"},
    {"face": "(¬▂¬)", "name": "Unimpressed"},
    {"face": "ヽ(♡‿♡)ノ", "name": "Cute Love"},
    {"face": "٩(◕‿◕｡)۶", "name": "Dancing"},
    {"face": "(´∀｀)", "name": "Grin"},
    {"face": "(✖╭╮✖)", "name": "Tired"},
    {"face": "(o_O)", "name": "Confused"},
    {"face": "(＠_＠;)", "name": "Nervous"},
    {"face": "(｡ŏ_ŏ)", "name": "Downcast"},
    {"face": "(ಠ‿ಠ)", "name": "Evil Smirk"},
    {"face": "(っ◕‿◕)っ", "name": "Friendly"},
    {"face": "(つ◉益◉)つ", "name": "Attack"},
    {"face": "(づ￣ ³￣)づ", "name": "Big Hug"},
    {"face": "⊂(・▽・⊂)", "name": "Cute Hug"},
    {"face": "(ᗒᗣᗕ)՞", "name": "Frustrated"},
    {"face": "｡ﾟ(ﾟ´Д｀ﾟ)ﾟ｡", "name": "Sobbing"},
    {"face": "(¬‿¬)", "name": "Sneaky"},
    {"face": "( •̀ω•́ )", "name": "Confident"},
    {"face": "＼(º □ º l|l)/", "name": "Speechless"},
    {"face": "(＠＾－＾)", "name": "Smiling"},
    {"face": "(⌒_⌒;)", "name": "Awkward"},
    {"face": "(＃￣ω￣)", "name": "Hmph"},
    {"face": "(∗❛ั∀❛ั∗)", "name": "Excited Smile"},
    {"face": "(╥_╥)", "name": "Crying"},
    {"face": "(๑•́ ω •̀๑)", "name": "Sad Puppy"},
    {"face": "( ° ͜ʖ °)", "name": "Lenny Again"},
    {"face": "(╯︵╰,)", "name": "Sobbing"},
    {"face": "(=￣ω￣=)", "name": "Sleepy"},
    {"face": "(T_T)", "name": "Sad Tears"},
    {"face": "(〃￣︶￣〃)", "name": "Cheeky Smile"},
    {"face": "( ︶︿︶)", "name": "Disappointed"},
    {"face": "(ಠ‿↼)", "name": "Wink"},
    {"face": "(≧ω≦)", "name": "Joyful"},
    {"face": "(☆ω☆)", "name": "Amazed"},
    {"face": "(╯︵╰,)", "name": "Crying Again"}
]

# Get the query entered by the user
query = "{query}".lower()

# Filter the kaomojis based on the user query
filtered_kaomojis = [
    k for k in kaomojis if query in k["face"].lower() or query in k["name"].lower()
]

# Create Alfred output format
output = {"items": []}

for kaomoji in filtered_kaomojis:
    output["items"].append({
        "title": kaomoji["face"],
        "subtitle": kaomoji["name"],
        "arg": kaomoji["face"],
        "mods": {
            "cmd": {
                "arg": kaomoji["face"],
                "subtitle": f"Copy {kaomoji['face']} to clipboard"
            },
            "alt": {
                "arg": kaomoji["name"],
                "subtitle": f"Copy '{kaomoji['name']}' to clipboard"
            }
        }
    })

# Output the JSON for Alfred
print(json.dumps(output))
