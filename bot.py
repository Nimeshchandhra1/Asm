from pyrogram import Client,filters

app_id = f8f459d4ee20923d555041cfd18ddf1f
app_key = '1997542'
token = "1443581629:AAGsCCwVhSoYdpC6CQdrhFbPyk2hc4dW0_w"



app = Client("antiservicemessage", app_id, app_key, bot_token=token)

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
