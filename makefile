###### EDIT #####################
#Directory with ui and resource files
GUI_DIR = src/gui
#Qt resource files to compile
RESOURCES_DIR = oxygen-icons-png

RESOURCES = oxygen.qrc

#Directory for compiled resources
COMPILED_DIR = src/ui

#UI files to compile
UI_FILES = mainWindow.ui about.ui

#pyuic4 and pyrcc4 binaries
PYUIC = pyuic4
PYRCC = pyrcc4

#################################
# DO NOT EDIT FOLLOWING

COMPILED_UI = $(UI_FILES:%.ui=$(COMPILED_DIR)/ui_%.py)
COMPILED_RESOURCES = $(RESOURCES:%.qrc=$(COMPILED_DIR)/%_rc.py)

all : resources ui

resources : $(COMPILED_RESOURCES)

ui : $(COMPILED_UI)

$(COMPILED_DIR)/ui_%.py : $(GUI_DIR)/%.ui
	$(PYUIC) $< -o $@

$(COMPILED_DIR)/%_rc.py : $(RESOURCES_DIR)/%.qrc
	$(PYRCC) $< -o $@

clean :
	$(RM) $(COMPILED_UI) $(COMPILED_RESOURCES) $(COMPILED_UI:.py=.pyc) $(COMPILED_RESOURCES:.py=.pyc)
