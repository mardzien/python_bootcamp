class Document:

    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def render(self):
        # output = ""
        # for el in self.elements:
        #     output += el.render()
        return "\n".join([el.render() for el in self.elements])


class Element:
    def __init__(self, text):
        self.text = text + "\n"

    def render(self):
        return self.text

class HeaderElement(Element):
    def render(self):
        text = super().render()
        text += "="*(len(text)-1) + "\n"
        return text


class LinkElement(Element):
    def __init__(self, text, url):
        self.text = text
        self.url = url

    def render(self):
        return f"[{self.text}](http://{self.url})\n"

dokument = Document()
dokument.add_element(HeaderElement("Header"))
dokument.add_element(LinkElement("ABC", "wp.pl"))
dokument.add_element(Element("simple text"))
text = dokument.render()

with open("dokument.md", 'w') as f:
    f.write(text)

def test_render():
    dokument = Document()
    dokument.add_element(HeaderElement("Header"))
    dokument.add_element(LinkElement("ABC", "wp.pl"))
    dokument.add_element(Element("simple text"))

    expected = """Header
======

[ABC](http://wp.pl)

simple text
"""
    assert dokument.render() == expected
