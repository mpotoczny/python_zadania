'''
Zaimplementuj klasy odpowiedzialne za tworzenie dokumentów
w składni MarkDown. Stwórz klasę bazową Element
zawierającą podstawową implementację metody render()
oraz kilka jej klas pochodnych.
Stwórz klasę Document umożliwiającą wyrenderowanie dodanych elementów.
Przykład użycia:
# >>> document = Document()
# >>> document.add_element(HeaderElement('Header'))
# >>> document.add_element(LinkElement('ABC', 'abc.com'))
# >>> document.add_element(Element('Simple'))
# >>> document.render()
Header
======
(ABC)[http://abc.com]
Simple
'''

class Document:
    def __init__(self):
        self._elements = []

    def add_element(self, element):
        self.element = element
        self._elements.append(element)

    def render(self):
        for i in self._elements:
            print(i)

class Element:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return f'{self.content}'

class HeaderElement(Element):
    def __str__(self):
        return f'{self.content}\n{(len(self.content))*"="}'

class LinkElement(Element):
    def __init__(self, content, url):
        super().__init__(content)
        self.url = url

    def __str__(self):
        return f'({self.content})[http://{self.url}]'


document = Document()
document.add_element(HeaderElement('Header'))
document.add_element(LinkElement('ABC', 'abc.com'))
document.add_element(Element('Simple'))
document.render()

# lista obiektów typu Element
print(document._elements)




