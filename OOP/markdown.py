
class Document:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def render(self):
        output = ""
        for el in self.elements:
            output += el.render()
        return output

class Element:
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text


class HeaderElement(Element):
    def render(self):
        text = super().render()
        text += "\n"+"="*len(text)


class LinkElement(Element):
    def __init__(self, text, url):
        super().__init__(text)
        self.url = url

    def render(self):
        return f"({self.text})[http://{self.url}]"



def test_render():
    dokument = Document()
    dokument.add_element(HeaderElement("Header"))
    dokument.add_element(LinkElement("ABC", "wp.pl"))
    dokument.add_element(Element("simple text"))

    expected ="""Header
    ======
    (ABC)[http://wp.pl]
    simple text
    """

    assert dokument.render() == expected