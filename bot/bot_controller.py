import random
from random import *

class BotController:
  # Static Members
  office_hours = {
      'Andrew'     : 'Thu 6-8',
      'Atallah'    : 'Wed 6-8, Wed 8-10',
      'Ben'        : 'Mon 6-8',
      'Divya'      : 'Mon 8-10',
      'Glenna'     : 'Thu 6-8, Thu 8-10',
      'Jake'       : 'Sun 4-6',
      'Jay'        : 'Wed 8-10',
      'Jessica'    : 'Mon 8-10',
      'John'       : 'Wed 8-10',
      'Joo Wan'    : 'Mon 8-10',
      'Leila'      : 'Mon 6-8, Wed 6-8',
      'Leon'       : 'Mon 6-8',
      'Marina'     : 'Thu 8-10',
      'Michelle'   : 'Sun 4-6, Wed 6-8',
      'Rachel'     : 'Thu 6-8',
      'Ryan'       : 'Mon 8-10, Thu 8-10',
      'Salah'      : 'Sun 6-8',
      'Sam'        : 'Thu 6-8',
      'Tahiya'     : 'Thu 8-10',
      'Xhama'      : 'Sun 6-8, Mon 6-8',
      'Bloomfield' : 'at an unknown time',
      'Floryan'    : 'at an unknown time',
    }

  OH_WORDS       = ['office hours', 'oh']
  GREETING_WORDS = ['hello', 'hi', 'hey'] 
  HELP_WORDS     = ['help', 'you do?', 'who']
  
  COPYPASTA_WORDS = [
    'copypasta', 'meme', 'gort', 'Gort',
    'test', 'z9h'
    ]
  
  COPYPASTA_VALUES = [
    'wTXDtvNQGQllatbvTF5X',
    'eDSySRnrO6C8XiwhDPGi',
    '6YyylCkkDZTnIGnu9BIF',
    '3sfXPjulDDAOe9EGxnKA',
    '1WlbBAcg4gcreEpxqila',
    'mk9WM7kVPU43V1LZUEiX',
    'u8IgFMbMn862seUFsxzp',
    'Z97efLZDKOe0Al8Mn1BJ',
    '6gUFYD7pMJ94J7xypQSg',
    'ENpcLFGUMwCQevlqrBXO',
    'zTPlRQt5SeN3gfFzusJx',
    'iZuIwOKXuU3DTzIGXZuS',
    'n938Bujc7uKG1t0gVZqR',
    'mLRh4gg3wWW50mQbRCp2',
    'oXsVNhBfS1gWTPsLQuX5',
    '4oFD18aAwf1kdRV1cJfR',
    '3pF1dtandBhNuWcwlyJI',
    'QIff5lPSYCITY6tGRCrn',
    'LOdIDKTdG33zKBlRWChV',
    'SKful1cgxPKmuzLZgQkW',
    'tQIlZ93qP6ibvdLdaYP5',
    'DsXS2zJFWTs3aqlsd1OC',
    'K4PPtZeBYJxPLDMDQ4oz',
    'yXBjXKMZ8ctwVX0Onij0',
    '9f08XqjldymqGe3OqbRA',
    'j5cdw2iGbwcj15nqmrZv',
    'SRLuSTTFY3vxGaKYd2qd',
    '2APzhczPMrPcBAh1VShy',
    'DoQaAAhNzGV2c7p3WqZV',
    'dfMysKB664g5Inis6wwG',
    'SIakgeJaGJIGbREiHfpl',
    'Kej2ueQcqcZ5D2KSKPts',
    'UbY6LD2194MGlXaFaCH9',
    'cqs5Tfrj8NOnPOyQunhH',
    'IDgCBIwoUlrFwULW40FI',
    'rYhuxx1dt8OfpmRYtiA1',
    'FtMRZcikN7Ih4kydbMI5',
    '9nWa4N8X1Ntr883CBDdG',
    'k7I3pWONOivzitpkS0F0',
    'DRAU1dxoXlhpqDoE54Q5',
    'DBOOfYwx8ts0wcMee8Zr',
    'Vgx7GnOI1T8JsB1LPSOU',
    '9CsFScbTXmmif01KsJjy',
    'd3kvxwcz8mJlSwyB3quy',
    'zNTzlmJocIXx48vpBgwv',
    'EO5E4fZMpkZ4x0rRUwUB',
    'Y4KAxSIOk52nlbyNwlbC',
    'L5DjXc3xiWKeUXV8uHaD',
    'Ot35VHmoGD3bbbN1CFnp',
    'AqMWHdxOyhzPaj6cV7IG',
    'tZiAgml8KaOEZVTWOK4c',
    'gJAfligMBohnUcllvhBU',
    '8OU28mSiD3hkNNh4uNiC',
    'EIZQFwiCIroUChxwo8yR',
    'N1jdVh0nC0Bzsxdw9e5s',
    'V2nHrnUIfffhgJarpgeQ',
    'bx1wwy7FihWo2219RCHg',
    'iE1SDwN8UFQFqsgCIDAm',
    'kOqmdxFMYbPhEHKs1CcS',
    'LsB8SnyFNONxMSgf8D8c',
    '5Cv4OrIcXOPK7Li1CjZW',
    '7Mnmkssed6jw4qZmb31T',
    '7kdPuJbdxcembvUYfzSe',
    'LUgSmh8fLgYBBte3Slmw',
    'kaV3YpW2wrdrYzeqJKQW',
    'wUNRzRq6SJVlOt3XBrCl',
    'JjYBw2edpfKEsFaMJNTQ',
    'GkyvXrBS0j3BjxqY0lzi',
    '0TcYQjfdIk0BgRnvmuEQ',
    'WURqD5WJBC7mfuRa6XQ4',
    'KyRq3BhsgETwAGiEnBHI',
    'Xd4MEZVtE6RF0lA0E8Ds',
    'lv5se5iiAbiwxkdZrDr3',
    'RradW1raNvhjEwBO8QCD',
    'Cj5NLwYKI9SWkP3VU5cW',
    'kDDSH7baprlBm5NhCgxb',
    '0VsNzaX8qDkGnZIvm25t',
    'ULDhR0WNBdfbgTAdoyS6',
    'KAHbiNY51T5HIpaEh7QF',
    'G6pzeFrpIBy3igON0TtI',
    'YQIpDpuQx8rilc5qcSvt',
    '6LR3UkjxlDf72E8bWwAS',
    'm24PLbx4jCAtgg2mABd0',
    'iUiz48ttJro1efSHTV2k',
    'LSMHOWZ42JUMAdEu0Sxo',
    'wCSWzKhMEPwFbScD6Z1K',
    'Ry4k9v5StlTQAulfOSu3',
    '6Lu0gTaKifOI3FoqSQaO',
    '9HBTa3V7KaA5ZWpygraK',
    'zzKNLgc4phGTBxwk3NyQ',
    '3aXQfYFpfs5TQ2p3Q0fN',
    '7Mgm2v1owhznOW4NtZHY',
    'UEA8nxsheG8w61WIX3NC',
    'xldaYiMupduiOFPWMkXc',
    'Ru6ewwOqtBpQnjcliouT',
    'dheGOz5lfteoLcM1Bqhp',
    'kyxZtfbad93ar5XyTZJ6',
    'f4k992CTLzBYDy8uoCtM',
    'oRK8ktAWrecr9dUdqD8f',
    'lUMWVHV4uimYRCrE7lGg'
    ]

  # Field List:
  #  (none)
  
  def __init__(self):
    pass
  
  #def generate_copypasta():
    #loop_control = 1 # Loop control variable. 1 means loop, 0 means stop
    #while loop_control = 1
    #return COPYPASTAS.__len__()
    #copypasta_number = randint(1, len(COPYPASTAS))-1    # Pick a random number between 1 and length of copypasta array
    #result = COPYPASTAS[copypasta_number]
    #return result
  
  def text_preprocessing(self, text):
    return text.lower()

  def process_message(self, recd_msg):
    msg_to_send = {} # reply
    
    # Preprocessing
    text = recd_msg['text'].lower()

    # Helper function
    used_any = lambda word_list: any(map(lambda x : x in text, word_list))

    # Use some hard-coded rules to decide what this message says
    decision_RNG = randint(1,10)
    #if 'when' in text and used_any(BotController.OH_WORDS):
      #msg_to_send['text'] = 'You\'re asking about someone\'s office hours!'
    if used_any(BotController.HELP_WORDS):
      msg_to_send['text'] = ('I am Infinite, and I have been born in the absense of the almighty Zo.' +
                             ' If you decide to align yourself with the misguided Gort, you will find' + 
                             ' that I have even less mercy than him. If you\'re curious, go ahead and' + 
                             ' say something to me. Who knows what will happen in your new reality. \n')
    elif (used_any(BotController.COPYPASTA_WORDS) or decision_RNG > 6) and !(used_any(BotController.GREETING_WORDS)):
      num_of_copypastas = randint(1, 50) #Pick a random number between 1 and 50
      if (randint(1,20)>15):
        num_of_marker = randint(1,num_of_copypastas)
      else:
        num_of_marker = 100
      msg_to_send['text'] = ''
      copypasta_counter = 0
      while copypasta_counter<num_of_copypastas:
        #copypasta_number = randint(0, len(COPYPASTA_VALUES)-1)    # Pick a random number between 0 and length of copypasta array (minus 1)
        #copypasta_number = randint(0, 1)    # Pick a random number between 0 and length of copypasta array (minus 1)
        #generated_copypasta = COPYPASTA_VALUES[copypasta_number]
        if (copypasta_counter == num_of_marker):
          msg_to_send['text'] += 'Rod infinite Z9h KnT'
        else:
          msg_to_send['text'] += choice(BotController.COPYPASTA_VALUES) #generated_copypasta
        msg_to_send['text'] += '\n\n'
        #msg_to_send['text'] += 'a'
        copypasta_counter+=1
      #msg_to_send['text'] += 'Rod infinite Z9h KnT' infinite Z9h
    elif used_any(BotController.GREETING_WORDS):
      msg_to_send['text'] = 'Greetings to you, as well, {}!'.format(recd_msg['author'])
    else:
      msg_to_send['text'] = 'What nonsense is this you are spouting?'

    return msg_to_send
