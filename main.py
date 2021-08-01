from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

from ankioku.Deck import Deck
from ankioku.Card import Card


KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "Ankioku"

    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch(*args)


<Tab>

    MDLabel:
        id: label
        text: "Home"
        halign: "center"
'''


class Tab(MDFloatLayout, MDTabsBase):  # type: ignore
    '''Class implementing content for a tab.'''


class Ankioku(MDApp):  # type: ignore
    def build(self):  # type: ignore
        return Builder.load_string(KV)

    def on_start(self) -> None:
        self.root.ids.tabs.add_widget(Tab(title="Home"))
        self.root.ids.tabs.add_widget(Tab(title="Decks"))
        self.root.ids.tabs.add_widget(Tab(title="Cards"))
        self.root.ids.tabs.add_widget(Tab(title="Sharing"))

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):  # type: ignore
        if tab_text == "Decks":
            d = Deck('A test deck')
            instance_tab.ids.label.text = repr(d)
        elif tab_text == "Cards":
            c = Card()
            c.question = "What color is the sky?"
            c.answer = "Blue"
            instance_tab.ids.label.text = repr(c)
        else:
            instance_tab.ids.label.text = tab_text


Ankioku().run()
