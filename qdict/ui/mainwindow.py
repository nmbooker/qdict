#! /usr/bin/env python

"""The qdict main window."""

from PyQt4 import QtCore, QtGui

import ui_mainwindow
import formatter
import dictclient

class MainWindow(QtGui.QMainWindow, ui_mainwindow.Ui_MainWindow):
    """The qdict main window.
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.go_button, QtCore.SIGNAL('clicked()'), self.define)

    def define(self):
        """Define the user's word."""
        server = dictclient.Connection()
        word = self.query_editor.text()
        definitions = server.define("*", word)
        if not definitions:
            return "<h1>No defintions for &quot;%s&quot;</h1>" % word
        html = "<h1>Definitions for &quot;%s&quot;</h1>" % word
        for definition in definitions:
            html += self.format_definition(definition)
        self.textBrowser.setHtml(html)
    
    def format_definition(self, definition):
        """Format a definition object.  Returns HTML in a string."""
        text = definition.getdefstr()
        word = definition.getword()
        dbname = definition.getdb().getname()
        return "<h2>%s</h2>\n%s" % (dbname, formatter.DefinitionFormatter(text).format())
