from os import environ
from pyrogram import Client,filters

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')

app = Client('asm',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)



DONATESTARTTEXT = """
text  
"""




@app.on_message(filters.private)
def start(c,m):
    m.reply(DONATESTARTTEXT,
)

@app.on_message(filters.group & filters.command("command@botname"))
def main(c,m):
    m.reply("""text""")

@app.on_message(filters.group & filters.command("command"))
def main(c,m):
    m.reply("""text""")



@app.on_message(filters.service)
def service(c,m):
    m.delete()


app.run()
