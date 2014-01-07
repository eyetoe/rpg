#!/usr/bin/env python
import curses
try:
    import npyscreen
except ImportError:
    print "The npyscreen module could not be imported. Get it at:"
    print "    http://code.google.com/p/npyscreen/"

TEXT = """
  ______                  _____ __          __ _____  _______  _____  _    _ 
 |  ____|                / ____|\ \        / /|_   _||__   __|/ ____|| |  | |
 | |__  _ __  ___   ___ | (___   \ \  /\  / /   | |     | |  | |     | |__| |
 |  __|| '__|/ _ \ / _ \ \___ \   \ \/  \/ /    | |     | |  | |     |  __  |
 | |   | |  |  __/|  __/ ____) |   \  /\  /    _| |_    | |  | |____ | |  | |
 |_|   |_|   \___| \___||_____/     \/  \/    |_____|   |_|   \_____||_|  |_|
           _____ ____     ____ _     ___            
          |  ___/ ___|   / ___| |   |_ _|           
          | |_  \___ \  | |   | |    | |            
          |  _|  ___) | | |___| |___ | |            
          |_|   |____/   \____|_____|___|           
"""


class CommandWidget(npyscreen.Autocomplete):
    commands = {
        'argle': {
            'help_text': "Argle your bargle like it was a fargle.",
            'args': (
                ['foo', 'bar'],
                ['baz', 'bang', 'biff']
            ),
        },
        'whizz': {
            'help_text': "Nothing like a little whizz to increase your fizz.",
        },
    }

    def auto_complete(self, keycode):
        if not self.value:
            suggestions = self.commands.keys()
            self.value = suggestions[self.get_choice(suggestions)]
        if not self.value[-1].isalnum():
            curses.beep()
            return
        self.value = self.value + ' '
        self.cursor_position = len(self.value)

class MainForm(npyscreen.FormMutt):
    COMMAND_WIDGET_CLASS = CommandWidget
    MAIN_WIDGET_CLASS = npyscreen.Pager

    def afterEditing(self):
        self.parentApp.NEXT_ACTIVE_FORM = None

    def create(self):
        super(MainForm, self).create()
        self.wStatus1.value = self.name
        self.wStatus2.value = 'status area'
        self.wMain.values = TEXT.split('\n')


class Application(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', MainForm, name='FreeSwitch CLI')


if __name__ == '__main__':
    app = Application().run()
