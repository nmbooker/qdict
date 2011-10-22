all: ui_mainwindow.py

ui_mainwindow.py: ui_mainwindow.ui
	pyuic4 -o ui_mainwindow.py -x ui_mainwindow.ui

clean::
	$(RM) ui_mainwindow.py
