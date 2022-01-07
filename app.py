import sys
import webbrowser
import PySimpleGUI as sg
import queue
import threading

import main
import base64
import os

import setting

ver = "1.1.9"
noob = "https://discord.gg/pQysP43P"
try:
    button_joiner = base64.b64encode(open("AlphaToolLogo.png", "rb").read())
    rtb_icon = base64.b64encode(open("icon.png", "rb").read())
except Exception as e:
    print(e)
    rtb_icon = b''
    button_joiner = b''


def long_operation_thread():

    main.start_spam()


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def the_gui():
    # sets theme
    # discordtokens = setting.tokens
    # f = open("Token.txt", 'w')
    # f.write(discordtokens)
    # f.close()
    sg.ChangeLookAndFeel('DarkBlack')
    gui_queue = queue.Queue()

    menu_def = [
        ['&About', ['Info','Donation']],
        ['&Config', ['Message']],
        ['&Support', ['DiscordServer', 'YouTube', 'Twitter']],
        ['&Terms of Service', ['terms of service']],
        ['&Execution and End', ['Exit', 'Run']]
    ]
    # 位置

    # Main Layout
    layout = [
        [sg.Menu(menu_def)],
        [sg.Image(data=button_joiner, size=(400, 250))],
    ]
    # Window options
    window = sg.Window(f'!Old!AlphaTool ver {ver}', layout, default_element_size=(40, 1), grab_anywhere=False,
                       location=(5, 5), icon=rtb_icon)

    while True:

            event, values = window.read(timeout=1000)
            if event is None:
                sys.exit()
            # If exit button is clicked
            elif event == "Message":
                while True:
                 #   window.Close()
                    menu_def = [


                        ['&Execution and End', ['Exit', 'Run']],
                    ]
                    layout = [
                        [sg.Menu(menu_def)],
                        [sg.Multiline(default_text='Test',
                                    size=(95, 15), key='user_text', font=('Segoe UI Semibold', 12), text_color="#eb3434")],

                    ]
                    window = sg.Window(f'!Old!AlphaTool ver {ver}', layout, default_element_size=(40, 1),
                                       grab_anywhere=False,
                                       location=(5, 5), icon=rtb_icon)
                    event, values = window.Read()
                    setting.user_text = values['user_text']
                    if event is None:
                        window.Close()
                        the_gui()

                    elif event == "Exit":
                         sys.exit()
                    # If run button is clicked
                    elif event == 'Run':
                #  window['Run'].update(disabled=True)
                         window.TKroot.title(f'!Old!AlphaTool ver {ver} Under attack')

                         setting.user_text = values['user_text']

                         try:
                              threading.Thread(target=long_operation_thread,
                                     args=(), daemon=True).start()
                         except Exception as e:
                                   print('Error')

                # Checks for incoming messages from threads
                         try:
                # get_nowait() will get exception when Queue is empty
                             message = gui_queue.get_nowait()
                         except queue.Empty:
                # break from the loop if no more messages are queued up
                                 message = None
                # if message received from queue, display the message in the Window
                         if message:
                                   print('Got a message back from the thread: ', message)

                                   print('event＝', event, '、values＝', values)
                         if event is None:
                                       window.Close()
                                       the_gui()
            elif event == "Donation":
                window.Close()

                layout = [

                    [sg.Text("あるふぁ#0810", font=('Segoe UI Semibold', 12))],
                ]
                window = sg.Window(f'!Old!AlphaTool ver {ver}', layout, default_element_size=(40, 1),
                                   grab_anywhere=False,
                                   location=(5, 5), icon=rtb_icon)
                event, values = window.Read()
                if event is None:
                    window.Close()
                    the_gui()
            elif event == "Info":
                while True:
                    window.Close()
                    frame = [
                        [sg.Text(
                            f" Alpha :)", font=('Segoe UI Semibold', 12))]
                    ]
                    layout = [

                        [sg.Text("AlphaTool", font=('Segoe UI Semibold', 12))],
                        [sg.Text("DiscordTool", font=('Segoe UI Semibold', 8))],
                        [sg.Text("AltCrater", font=('Segoe UI Semibold', 8))],
                        [sg.Text("NitroGen", font=('Segoe UI Semibold', 8))],
                        [sg.Text("TokenLoggerCrater", font=('Segoe UI Semibold', 8))],
                        [sg.Text("Version {}".format(ver), font=('Segoe UI Semibold', 12))],
                        [sg.Text("AlphaTool", font=('Segoe UI Semibold', 12))],
                        [sg.Frame("Credits:", frame, font="Any 15")],
                    ]
                    window = sg.Window(f'!Old!AlphaTool ver {ver}', layout, default_element_size=(40, 1),
                                       grab_anywhere=False,
                                       location=(5, 5), icon=rtb_icon)
                    event, values = window.Read()
                    if event is None:
                        window.Close()
                        the_gui()
            elif event == "terms of service":
                sg.popup("""
絶対にpngファイルは消さないでください。、
利用規約
この利用規約（以下，「本規約」といいます。）は，あるふぁ（以下，「当社」といいます。）がこのアプリ上で提供するサービス（以下，「本サービス」といいます。）の利用条件を定めるものです。遊んでいただいてくれている皆さま（以下，「ユーザー」といいます。）には，本規約に従って，本サービスをご利用いただきます。

第1条（適用）
本規約は，ユーザーと当社との間の本サービスの利用に関わる一切の関係に適用されるものとします。
当社は本サービスに関し，本規約のほか，ご利用にあたってのルール等，各種の定め（以下，「個別規定」といいます。）をすることがあります。これら個別規定はその名称のいかんに関わらず，本規約の一部を構成するものとします。
本規約の規定が前条の個別規定の規定と矛盾する場合には，個別規定において特段の定めなき限り，個別規定の規定が優先されるものとします。
第2条（禁止事項）
ユーザーは，本サービスの利用にあたり，以下の行為をしてはなりません。

法令または公序良俗に違反する行為
犯罪行為に関連する行為
本サービスの内容等，本サービスに含まれる著作権，商標権ほか知的財産権を侵害する行為
当社，ほかのユーザー，またはその他第三者のサーバーまたはネットワークの機能を破壊したり，妨害したりする行為
本サービスによって得られた情報を商業的に利用する行為
当社のサービスの運営を妨害するおそれのある行為
不正アクセスをし，またはこれを試みる行為
他のユーザーに関する個人情報等を収集または蓄積する行為
不正な目的を持って本サービスを利用する行為
本サービスの他のユーザーまたはその他の第三者に不利益，損害，不快感を与える行為
他のユーザーに成りすます行為
当社が許諾しない本サービス上での宣伝，広告，勧誘，または営業行為
面識のない異性との出会いを目的とした行為
当社のサービスに関連して，反社会的勢力に対して直接または間接に利益を供与する行為
その他，当社が不適切と判断する行為
第3条（本サービスの提供の停止等）
本サービスについて，利用者が著しく低下した場合
当社が本サービスの利用を適当でないと判断した場合
当社は，本条に基づき当社が行った行為によりユーザーに生じた損害について，一切の責任を負いません。

第4条（権利義務の譲渡の禁止）
ユーザーは，当社の書面による事前の承諾なく，利用契約上の地位または本規約に基づく権利もしくは義務を第三者に譲渡し，または担保に供することはできません。

第5条（準拠法・裁判管轄）
本規約の解釈にあたっては，日本法を準拠法とします。
本サービスに関して紛争が生じた場合には，当社の本店所在地を管轄する裁判所を専属的合意管轄とします。
第6条（利用登録）
DiscordServerでの30人の招待(サブアカウント等のFakeは無効)を達成(もしくはpremiumUser)し，当社がこれを承認することによって，利用登録が完了するものとします。
当社は，利用登録の申請者に以下の事由があると判断した場合，利用登録の申請を承認しないことがあり，その理由については一切の開示義務を負わないものとします。
利用登録の申請に際して虚偽の事項を届け出た場合
本規約に違反したことがある者からの申請である場合
その他，当社が利用登録を相当でないと判断した場合
                     
                     """, font=('Segoe UI Semibold', 8))

            elif event == "Exit":
                sys.exit()
            # If run button is clicked
            elif event == 'Run':
                #  window['Run'].update(disabled=True)
                window.TKroot.title(f'!Old!AlphaTool ver {ver} Under attack')
                #  setting.nitro = values['nitro']
               # setting.iterations = values['iterations']
              #  setting.user_text = values['user_text']
               # setting.Syoutai = values['Syoutai']
                #setting.shrek_script = values['shrek_script']

             #   if values['shrek_script']:
              #      setting.shrek_script = True
               # else:
                #    setting.shrek_script = False
                # Calls the long_operation_thread
                try:
                    threading.Thread(target=long_operation_thread,
                                     args=(), daemon=True).start()
                except Exception as e:
                    print('Error')

            # Checks for incoming messages from threads
            try:
                # get_nowait() will get exception when Queue is empty
                message = gui_queue.get_nowait()
            except queue.Empty:
                # break from the loop if no more messages are queued up
                message = None
            # if message received from queue, display the message in the Window
            if message:
                print('Got a message back from the thread: ', message)

            elif event == "Twitter":
                webbrowser.open("https://twitter.com/Ika34Zuki")
            elif event == "YouTube":
                webbrowser.open("https://www.youtube.com/channel/UCykJ_FngukPaSQKNzSYLT5g")
            elif event == "DiscordServer":

                webbrowser.open("https://discord.gg/dhnCSAH8KE")
            elif event == "Donation":
                window.Close()

                layout = [

                    [sg.Text("あるふぁ#0810", font=('Segoe UI Semibold', 12))],
                ]
                window = sg.Window(f'!Old!AlphaTool ver {ver}', layout, default_element_size=(40, 1),
                                   grab_anywhere=False,
                                   location=(5, 5), icon=rtb_icon)
                event, values = window.Read()
                if event is None:
                    window.Close()
                    the_gui()
            elif event == "Info":
                while True:
                    window.Close()
                    frame = [
                        [sg.Text(
                            f" Alpha :)")]
                    ]
                    layout = [

                        [sg.Text("Version {}".format(ver))],

                        [sg.Frame("Credits:", frame, font="Any 15")],
                    ]
                    window = sg.Window(f'!Old!AlphaTool ver {ver}', layout, default_element_size=(40, 1),
                                       grab_anywhere=False,
                                       location=(5, 5), icon=rtb_icon)
                    event, values = window.Read()
                    if event is None:
                        window.Close()
                        the_gui()
    # if user exits the window, then close the window and exit the GUI
#    window.close()


if __name__ == '__main__':
    the_gui()
    print('End')
