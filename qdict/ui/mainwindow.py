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
        self.connect(self.query_editor, QtCore.SIGNAL('returnPressed()'), self.define)
        self.connect(self.query_editor, QtCore.SIGNAL('textChanged(QString)'), self.switch_go_button)
        self.connect(self.clear_button, QtCore.SIGNAL('clicked()'), self.clear_input)
        self.switch_go_button()

    def define(self):
        """Define the user's word."""
        word = self.query_editor.text()
        try:
            server = dictclient.Connection()
            definitions = server.define("*", word)
        except Exception, exc:
            self.report_error(str(exc))

        if not definitions:
            self.textBrowser.setHtml("<h1>No definitions for &quot;%s&quot;</h1>" % word)
            QtGui.QMessageBox.information(self, "Word not found",
                    "No definition found for %s" % word)
            return
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

    def clear_input(self):
        """Clear and focus the word box."""
        self.query_editor.clear()
        self.query_editor.setFocus()


    def report_error(self, error):
        """Report an error retrieving definitions."""
        QtGui.QMessageBox.critical(self,
                    "QDict Error - Couldn't retrieve definition",
                    "Couldn't get definition: %s" % error,
                    )

    def switch_go_button(self):
        """Decide and set whether the Go button should be clickable."""
        self.go_button.setEnabled(not self.query_editor.text().isEmpty())
