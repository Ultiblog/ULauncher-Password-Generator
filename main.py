import string
import random
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction


class DemoExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')
        random.shuffle(characters)

        for i in range(5):

            password = []
            length = random.randint(12,18)

            for i in range(length):
                password.append(random.choice(characters))

            random.shuffle(password)
            password = ''.join(password)

            items.append(ExtensionResultItem(icon='images/lock.png',
                                            name=password,
                                            description='Random generated password ',
                                            on_enter=CopyToClipboardAction(password)))

        return RenderResultListAction(items)


if __name__ == '__main__':
    DemoExtension().run()
