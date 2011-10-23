#! /usr/bin/env python

"""Helpers to format definition text as HTML."""

class DefinitionFormatter(object):
    """Puts line breaks in expected places."""
    def __init__(self, text):
        self.text = text
        self.lines = text.split('\n')
    
    def format(self):
        paragraphs = []
        for line in self.lines:
            paragraphs.append("<p>%s</p>" % line.strip())
        return '\n'.join(paragraphs)
