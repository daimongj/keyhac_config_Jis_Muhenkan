import sys
import os
import datetime

import pyauto
from keyhac import *										

#JisMuhenkan_Simple_20221204_config.py for keyhac
#使い方 Keyhac.exeのあるフォルダのConfig.pyをこのテキストで全て書き換える
#
#GdriveにあるJisMuhenkan_Simpleというファイル名が付いたテキストは、【無変換】キーをモディフィアキーとして使う前提のキーカスタマイズの設定。左親指で【無変換】キー押しながらカーソル移動などを行う。
#
#内容は、カーソルの移動、【Enter】【Esc】【Tab】キーの置き換え、最初のメニューの表示、タスクビューの表示、クリップボード履歴からの貼り付け、他のキーと【無変換】キーの組み合わせは【Ctrl】キーとの組み合わせと同じ
#タスクトレイのKeyhacアイコンを右クリックで”設定のリロード”
#Keyhacを終了するとキー配列は元に戻る
#【無変換】キーは基本的に【CTRL】キーと同じ機能。ただし一部のキーの組み合わせをカーソル移動や違う文字の入力用に使ってる
#例 メモ帳でテキストを開き【無変換】を押しながら【L】を押すとカーソルが右に移動
#【Shift】＋【無変換】+【L】でカーソルの右方向に文字が選択される
#その後【無変換】+【H】を押すと選ばれた文章が削除
#【無変換】+【Z】で元に戻る。【Ctrl】＋【Z】と同じ
#【無変換】+【I】,J,K,Lはカーソルの移動の上、左、下、右
#【無変換】+【Y】,U,O,PはPageUp,Home,End,PageDown 【無変換】+【H】でBS
#【無変換】+【N】はEnter　＋【T】はTab　＋【Q】はEsc　＋【W】は最初のメニュー（Altを押した後に↓）を開いた状態にする。解除は【無変換】+【Q】を2回押す
#【無変換】+【M】でタスクビュー
#【無変換】+【B】でクリップボードの履歴から貼り付け、さらに【無変換】+【L】で定型文、さらに【無変換】+【L】で日時の貼り付け

s0Shift=""
sLShift="LShift-"
sLAlt="LAlt-"
sLAlt ="RCtrl-"
#sLalt="USER0"
sLCtrl="LCtrl-"
sRCtrl="RCtrl-"
sLRCtrl = "LCtrl-RCtrl-"
sRLCtrl = "LCtrl-RCtrl-"
sLShiftRCtrl = "LCtrl-RCtrl-"
sLCtrl2 = "LCtrl-User2-"
sRCtrl2 = "RCtrl-User2-"
sLCtrl3 = "LCtrl-User3-"
sRCtrl3 = "RCtrl-User3-"
TouchpadHome="(172)"	#TouchpadHome
TouchpadPhone="(181)"	#TouchpadPhone
TouchpadFolder="(182)"	#TouchpadFolder
nMuhenkan=29		# 無変換	
sMuhenkan="(29)"		# 無変換
nHenkan=28		  # 変換
sHenkan="(28)"		  # 変換
nHiragana=242	   # ひらがな
sHiragana="(242)"	   # ひらがな
# (243)	半角/全角
# (244)	半角/全角
# C-(3)	Break
sComma="(188)"		  # ,
sPeriod="(190)"		 # .  
sSlash="(191)"		  # /
sAtmark="(192)"		 # @
sMaruKakkoHidari="(40)" # paren 丸括弧 (
sParenLeft="(40)"	   # paren 丸括弧 (
sMaruKakkoHidari="(41)" # paren 丸括弧 )
sParenRight="(41)"	  # paren 丸括弧 )
sColon="(186)"		   # colon コロン :
sSemiColon="(187)"	   # semicolon セミコロン ;
sFutougouHidari="(60)"  # less than 不等号 
sLessThan="(60)"		# less than 不等号 <
sFutougouMigi="(62)"	# greater than 不等号 >
sGreaterThan="(62)"	 # greater than 不等号 >
sKakuKakkoHidari="(219)" # bracket 角括弧 [ 
sBracketLeft="(219)"	 # bracket 角括弧 [ 
sBackslash="(220)"	   # backslash \
sYen="(220)"			 # 円マーク \ 226 (222)	^
sKakuKakkoMigi="(221)"   # bracket 角括弧 ]
sBracketRight="(221)"	# bracket 角括弧 ]
sNamiKakkoHidari="(123)"# brace波括弧 {
sBraceLeft="(123)"	  # brace波括弧 {
sTateBou="(124)"		# |
sNamiKakkoMigi="(125)"  # brace波括弧 }
sBraceRight="(125)"	 # brace波括弧 }
nPause=19	 # brace波括弧 }
sPause="(19)"	 # brace波括弧 
nMod1=255

sPlus = sLShift + "SemiColon"
sTasu = sLShift + "SemiColon"
sKakeru = sLShift + "Colon"
sEql = sLShift + "Minus"
sAnd = "Shift-" + "6"
sCaret = "Caret"
sKara = "Shift-" + "Caret"
sBackslash = "BackSlash"
sUnderbar = "Shift-" + sBackslash

sDQT = sLShift + "2"
sSQT = sLShift + "7"

sUser0 = "User0-"
sUser1 = "User1-"

def configure(keymap):

	# User modifier key definition
	# keymap.defineModifier( 235, "User0" )
	keymap.replaceKey(sMuhenkan, "RCtrl")  #【無変換】を RCtrl キーに
	# Global keymap which affects any windows
	keymap.setFont( "ＭＳ ゴシック", 18 )
	# 定型文
	fixed_items = [
	    ( "定型文 name@server.net",           "name@server.net" ),
	    ( "config.pyを編集",           keymap.command_EditConfig ),
	    ( "config.pyをリロード",       keymap.command_ReloadConfig ),
	    ( "起動 ぷちらんちゃ",           keymap.ShellExecuteCommand(None,"../../ptlnc67i\ptlnc.exe","","") )
	]

	# 日時をペーストする機能
	def dateAndTime(fmt):
	    def _dateAndTime():
	        return datetime.datetime.now().strftime(fmt)
	    return _dateAndTime

	# 日時
	date_and_time_items = [
	    ( "YYYY/MM/DD HH:MM:SS",   dateAndTime("%Y/%m/%d %H:%M:%S") ),
	    ( "YYYY/MM/DD",            dateAndTime("%Y/%m/%d") ),
	    ( "HH:MM:SS",              dateAndTime("%H:%M:%S") ),
	    ( "YYYYMMDD_HHMMSS",       dateAndTime("%Y%m%d_%H%M%S") ),
	    ( "YYYYMMDD",              dateAndTime("%Y%m%d") ),
	    ( "HHMMSS",                dateAndTime("%H%M%S") ),
	]

	keymap.cblisters += [
	    ( "定型文",         cblister_FixedPhrase(fixed_items) ),
	    ( "日時",           cblister_FixedPhrase(date_and_time_items) ),
	    ]

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
		#for key in [chr(ord("A") + i) for i in range(26)]:
		for i in range(253):
			keymap_global["User0-(" + str(i+1) + ")"] = "RCtrl-("+ str(i +1)+ ")"
		for i in range(253):
			keymap_global["LShift-User0-(" + str(i+1) + ")"] = "LShift-RCtrl-("+ str(i+1) + ")"
		for i in range(253):
			keymap_global["RShift-User0-(" + str(i+1) + ")"] = "RShift-RCtrl-("+ str(i+1) + ")"
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
		keymap_global["LShift-User0-" + "I"] = "LShift-" + "Up"
		keymap_global["LShift-User0-" + "J"] = "LShift-" + "Left"
		keymap_global["LShift-User0-" + "K"] = "LShift-" + "Down"
		keymap_global["LShift-User0-" + "L"] = "LShift-" + "Right"
		keymap_global["LShift-User0-" + "U"] = "LShift-" + "Home"
		keymap_global["LShift-User0-" + "O"] = "LShift-" + "End"
		keymap_global["LShift-User0-" + "Y"] = "LShift-" + "PageUp"
		keymap_global["LShift-User0-" + "P"] = "LShift-" + "PageDown"
		keymap_global["LShift-User0-" + "H"] = "LShift-" + "Back"
		keymap_global["LShift-User0-" + "N"] = "LShift-" + "Enter"
		keymap_global["LShift-User0-" + "T"] = "LShift-" + "Tab"
		#
		keymap_global["RShift-User0-" + "I"] = "RShift-" + "Up"
		keymap_global["RShift-User0-" + "J"] = "RShift-" + "Left"
		keymap_global["RShift-User0-" + "K"] = "RShift-" + "Down"
		keymap_global["RShift-User0-" + "L"] = "RShift-" + "Right"
		keymap_global["RShift-User0-" + "U"] = "RShift-" + "Home"
		keymap_global["RShift-User0-" + "O"] = "RShift-" + "End"
		keymap_global["RShift-User0-" + "Y"] = "RShift-" + "PageUp"
		keymap_global["RShift-User0-" + "P"] = "RShift-" + "PageDown"
		keymap_global["RShift-User0-" + "H"] = "RShift-" + "Back"
		keymap_global["RShift-User0-" + "N"] = "RShift-" + "Enter"
		keymap_global["RShift-User0-" + "T"] = "RShift-" + "Tab"
		#
		keymap_global["User0-" + "W"] = "Alt","Down" # ALTを押してDown = 最初のメニューを呼び出す。その後カーソルで上下左右に移動する。取り消すには【無変換】+【Q】を2回押す
		keymap_global["User0-" + "Q"] = "Esc" # キャンセル、ポップアップウィンドウを閉じる
		keymap_global["User0-" + "B"] = keymap.command_ClipboardList # クリップボード履歴表示 さらに右カーソルで定型文の貼り付けやアプリの起動、さらに右カーソルで日時の貼り付けが出来る
		# LWin-Vでクリップボード履歴からペースト出来るが、Keyhacでモディファイアキーを使ったカーソル移動には対応しない。KeyHac内でもクリップボード履歴の活用は出来る。TaskClipはカーソル移動が出来る。TaskClipはクリップボードのテキスト形式データを保存し、再利用 https://www.vector.co.jp/soft/win95/util/se245727.html アプリの設定でホットキーを例えば CTRL+B にする
		keymap_global["User0-" + "M"] = "RWin-Tab"
		# keymap_global["User0-" + "M"] = keymap.ShellExecuteCommand(None,"../../TaskList\TaskList.exe","","") # tasklist Windows標準の[Alt]+[Tab]機能のポップアップウィンドウ版　https://www.vector.co.jp/soft/dl/win95/util/se149679.html
		#keymap_global["User0-" + "G"] = keymap.ShellExecuteCommand(None,"../../ptlnc67i\ptlnc.exe","","") # 　相対パス 自身の一つ上のディレクトリ ../　ランチャー　ぷちらんちゃ https://www.vector.co.jp/soft/dl/win95/util/se283207.html
		# メニューから使えばいいような機能は【無変換】+【W】経由で割り切る ＠192 E D 補完入力 独自Script Asroc等



