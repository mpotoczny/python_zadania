class Element:
    def __init__(self, content):
        self._content = content

    def __str__(self):
        return f"{self._content}"


class HeaderElement(Element):
    def __str__(self):
        return f"{self._content}\n{'='*len(self._content)}"


class LinkElement(Element):
    def __init__(self, content, url):
        super().__init__(content)
        self._url = url

    def __str__(self):
        return f"({self._content})[http://{self._url}]"


class Document:
    def __init__(self):
        self._elements = []

    def add_element(self, element: Element):

        if not isinstance(element, Element):
            raise TypeError('Element needs to be instance of Element')

        self._elements.append(element)

    def __str__(self):
        for el in self._elements:
            pass

    def render(self):
        pass


d1 = Document()
d1.add_element(HeaderElement("Napis"))
d1.add_element(LinkElement("Hiperłącze","www.cnn.com"))
d1.render()