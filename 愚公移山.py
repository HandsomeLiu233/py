from chatterbot import ChatBot

sb=ChatBot(
    'sb',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.outbot.TerminalAdapter',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

sb.train('chatterbot.corpus.chinese')
print('说点什么')
while True:
    bot_input=sb.get_response(None)