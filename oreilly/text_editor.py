"""Text Editor Task

I believe that many of you have dealt with such a problem. One day you are working in the text editor,
saving the document and closing it. And the next day you are re-reading the text and realizing
that one of the previous versions was better but there is no way to get it back.
This thing can be easily handled by the version control system (for example, git),
but it’s used mostly by the developers and not the ordinary people who work with texts.
In this mission you’ll help the latter by creating a text editor prototype that supports
the version control system, which will allow to save different versions of the text and restore any one of them.
Your task is to create 2 classes: Text and SavedText.
The first will works with texts (adding, font changing, etc.),
the second will control the versions and save them.

Class Text should have the next methods:
write(text) - adds (text) to the current text;
set_font(font name) - sets the chosen font.
Font is applied to the whole text, even if it’s added after the font is set.
The font is displayed in the square brackets before and after the text: "[Arial]...example...[Arial]".
Font can be specified multiple times but only the last variant is displays;
show() - returns the current text and font (if is was set);
restore(SavedText.get_version(number)) - restores the text of the chosen version.

Class SavedText should have the next methods:
save_text(Text) - saves the current text and font.
The first saved version has the number 0, the second - 1, and so on;
get_version(number) - this method works with the 'restore'
method and is used for choosing the needed version of the text.

Example:

1. text = Text()
2. saver = SavedText()
3.
4. text.write("At the very beginning ")
5. saver.save_text(text)
6. text.set_font("Arial")
7. saver.save_text(text)
8. text.write("there was nothing.")
9. text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
10.
11. text.restore(saver.get_version(0))
12. text.show() == "At the very beginning "
13.
14. Input: information about the text and saved copies.
15.
16. Output: the text after all of the commands.

Input: information about the text and saved copies.
Output: the text after all of the commands.
Precondition: No more than 10 saved copies.
"""

from dataclasses import dataclass
from copy import copy


@dataclass
class TextData:
    text: str = ""
    font: str = ""


class Text:
    def __init__(self) -> None:
        self.data = TextData()

    def write(self, text: str) -> None:
        """Adds (text) to the current text"""
        self.data.text += text

    def set_font(self, font_name: str) -> None:
        """Sets the chosen font"""
        self.data.font = f"[{font_name}]"

    def show(self) -> str:
        """Returns the current text and font (if it was set)"""
        data = self.data
        return f"{data.font}{data.text}{data.font}"

    def restore(self, text: TextData) -> None:
        self.data = text


class SavedText:
    def __init__(self) -> None:
        self.texts: list = []

    def save_text(self, text: Text) -> None:
        self.texts.append(copy(text.data))

    def get_version(self, number: int) -> Text:
        return self.texts[number]


if __name__ == "__main__":
    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    text_2 = Text()
    saver_2 = SavedText()
    text_2.write("Tomorrow at 7:15 PM.")
    saver_2.save_text(text_2)
    text_2.set_font("ComicSans")
    text_2.write(" Sorry. 7:15 AM.")
    saver_2.save_text(text_2)
    text_2.write(" Near the stadium.")
    text_2.restore(saver_2.get_version(1))
    assert text_2.show() == "[ComicSans]Tomorrow at 7:15 PM. Sorry. 7:15 AM.[ComicSans]"
