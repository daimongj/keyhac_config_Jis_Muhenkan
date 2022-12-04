import sys
import os
import datetime
import time
import copy

from ctypes import *
import pyauto
from keyhac import *
from ctypes import *

def configure(keymap):

	# User modifier key definition
	keymap.replaceKey( "29", 235 )
	keymap.defineModifier( 235, "User0" )

	def switch_ime(flag):
		if flag:
			ime_status = 1
		else:
			ime_status = 0

		# IMEのON/OFFをセット
		keymap.wnd.setImeStatus(ime_status)

	def ime_on():
		switch_ime(True)

	def ime_off():
		switch_ime(False)

	if 1:
		#User0（無変換） との組み合わせでカーソル移動や文字の削除やコピペを実現する
		#1-254
		#ABCDEFGHIJKLMNOPQRSTUVWXYZ
		#       HIJKL NOP   TU   Y  カーソル移動用キー
		#ABCDEFG     M   QRS  VWX Z Ctrl+で使うキー
		keymap_global = keymap.defineWindowKeymap()
		for i in range(253):
			keymap_global["User0-(" + str(i+1) + ")"] = "RCtrl-("+ str(i +1)+ ")"
		for i in range(253):
			keymap_global["LShift-User0-(" + str(i+1) + ")"] = "LShift-RCtrl-("+ str(i +1)+ ")"
		for i in range(253):
			keymap_global["RShift-User0-(" + str(i+1) + ")"] = "RShift-RCtrl-("+ str(i +1)+ ")"
		#
		keymap_global["User0-" + "I"] = "Up"
		keymap_global["User0-" + "J"] = "Left"
		keymap_global["User0-" + "K"] = "Down"
		keymap_global["User0-" + "L"] = "Right"
		keymap_global["User0-" + "U"] = "Home"
		keymap_global["User0-" + "O"] = "End"
		keymap_global["User0-" + "Y"] = "PageUp"
		keymap_global["User0-" + "P"] = "PageDown"
		keymap_global["User0-" + "H"] = "Back"
		keymap_global["User0-" + "N"] = "Enter"
		keymap_global["User0-" + "T"] = "Tab"
		#
		keymap_global["LShift-User0-" + "I"] = "LShift-Up"
		keymap_global["LShift-User0-" + "J"] = "LShift-Left"
		keymap_global["LShift-User0-" + "K"] = "LShift-Down"
		keymap_global["LShift-User0-" + "L"] = "LShift-Right"
		keymap_global["LShift-User0-" + "U"] = "LShift-Home"
		keymap_global["LShift-User0-" + "O"] = "LShift-End"
		keymap_global["LShift-User0-" + "Y"] = "LShift-PageUp"
		keymap_global["LShift-User0-" + "P"] = "LShift-PageDown"
		keymap_global["LShift-User0-" + "H"] = "LShift-Back"
		keymap_global["LShift-User0-" + "N"] = "LShift-Enter"
		keymap_global["LShift-User0-" + "T"] = "LShift-Tab"
		#
		keymap_global["RShift-User0-" + "I"] = "RShift-Up"
		keymap_global["RShift-User0-" + "J"] = "RShift-Left"
		keymap_global["RShift-User0-" + "K"] = "RShift-Down"
		keymap_global["RShift-User0-" + "L"] = "RShift-Right"
		keymap_global["RShift-User0-" + "U"] = "RShift-Home"
		keymap_global["RShift-User0-" + "O"] = "RShift-End"
		keymap_global["RShift-User0-" + "Y"] = "RShift-PageUp"
		keymap_global["RShift-User0-" + "P"] = "RShift-PageDown"
		keymap_global["RShift-User0-" + "H"] = "RShift-Back"
		keymap_global["RShift-User0-" + "N"] = "RShift-Enter"
		keymap_global["RShift-User0-" + "T"] = "RShift-Tab"
		#
		keymap_global["User0-" + "W"] = "Alt","Down"
		keymap_global["User0-" + "Q"] = "Esc"
		keymap_global["User0-" + "B"] = keymap.command_ClipboardList
		keymap_global["User0-" + "M"] = "RWin-Tab"



