class HelloWorld(object):
    """
    Simple test of the basic architecture of the project.
    """

    def __init__(self, text='Hello world!'):
        """
        Create an empty HelloWorld object.
        @param text: text to print. Set to 'Hello world!' if ommitted.
        """
        self._text = text

    def print_text(self):
        """
        Print the text stored inside of the object to the terminal.
        """
        print self._text
