from channels import Group


def ws_add(message):
    # Connected to websocket.connect
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    Group("chat").add(message.reply_channel)


def ws_message(message):
    # Connected to websocket.receive
    Group("chat").send({
        "text": "[user] %s" % message.content['text'],
    })


def ws_disconnect(message):
    # Connected to websocket.disconnect
    Group("chat").discard(message.reply_channel)