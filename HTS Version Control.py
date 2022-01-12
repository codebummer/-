from pywinauto import application, timings
# from pywinauto import timings
import time
import os

app = application.Application()
app.start("C:/KiwoomHero4/Bin/NKStarter.exe")

title = "영웅문 Login"
dlg = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=title))

pass_ctrl = dlg.Edit2
pass_ctrl.SetFocus()
pass_ctrl.TypeKeys('xxxx')

cert_ctrl = dlg.Edit3
cert_ctrl.SetFocus()
cert_ctrl.TypeKeys('yyyy')

btn_ctrl = dlg.Button0
btn_ctrl.Click()

time.sleep(90)
os.system("taskkill /im NKStarter.exe")



# import subprocess
# import win32gui
# import win32con
# import win32api
# import time


# def open_login_window(password, cert_password, secs=60):
#     """
#     OpenAPI+를 사용해서 로그인 윈도우를 실행한 후 로그인을 시도하는 함수
#     :param password: 비밀번호
#     :param cert_password: 공인인증 비밀번호
#     :param secs: 로그인 완료까지 대기할 시간
#     :return:
#     """
#     cmd = "C:/Users/ACECOM/AppData/Local/Programs/Python/venv37_32/Scripts/python.exe login.py"
#     subprocess.Popen(cmd, shell=True)
#     time.sleep(5)

#     try_manual_login(password, cert_password)

#     for i in range(secs):
#         print(f"로그인 완료 대기 중 {secs-i}")
#         time.sleep(1)


# def window_enumeration_handler(hwnd, top_windows):
#     top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


# def enum_windows():
#     windows = []
#     win32gui.EnumWindows(window_enumeration_handler, windows)
#     return windows


# def find_window(caption):
#     hwnd = win32gui.FindWindow(None, caption)

#     if hwnd == 0:
#         windows = enum_windows()
#         for handle, title in windows:
#             if caption in title:
#                 hwnd = handle
#                 break

#     return hwnd


# def enter_keys(hwnd, password):
#     win32gui.SetForegroundWindow(hwnd)
#     win32api.Sleep(100)

#     for c in password:
#         win32api.SendMessage(hwnd, win32con.WM_CHAR, ord(c), 0)
#         win32api.Sleep(100)


# def click_button(btn_hwnd):
#     win32api.PostMessage(btn_hwnd, win32con.WM_LBUTTONDOWN, 0, 0)
#     win32api.Sleep(100)
#     win32api.PostMessage(btn_hwnd, win32con.WM_LBUTTONUP, 0, 0)
#     win32api.Sleep(100)


# def set_auto_on(password):
#     hwnd = find_window("계좌비밀번호")

#     # 비밀번호등록
#     edit = win32gui.GetDlgItem(hwnd, 0xCA)
#     enter_keys(edit, password)
#     win32api.Sleep(100)
#     button_register_all = win32gui.GetDlgItem(hwnd, 0xCE)
#     click_button(button_register_all)

#     # 체크박스 체크
#     checkbox = win32gui.GetDlgItem(hwnd, 0xCD)
#     checked = win32gui.SendMessage(checkbox, win32con.BM_GETCHECK)
#     if not checked:
#         win32gui.SendMessage(checkbox, win32con.BM_SETCHECK, 0)

#     # 닫기 버튼 클릭
#     button= win32gui.GetDlgItem(hwnd, 0x01)
#     click_button(button)


# def set_auto_off():
#     try:
#         hwnd = find_window("계좌비밀번호")

#         # 체크박스 해제
#         checkbox = win32gui.GetDlgItem(hwnd, 0xCD)
#         checked = win32gui.SendMessage(checkbox, win32con.BM_GETCHECK)
#         if checked:
#             win32gui.SendMessage(checkbox, win32con.BM_SETCHECK, 0)

#         # 닫기 버튼 클릭
#         button= win32gui.GetDlgItem(hwnd, 0x01)
#         click_button(button)
#     except:
#         print("auto 해제 실패")

#     print("auto 해제 후 대기 중")
#     time.sleep(5)

# def try_manual_login(password, cert_password):
#     hwnd = find_window("Open API Login")
#     if hwnd == 0:
#         return

#     edit_pass = win32gui.GetDlgItem(hwnd, 0x3E9)
#     edit_cert = win32gui.GetDlgItem(hwnd, 0x3EA)
#     button = win32gui.GetDlgItem(hwnd, 0x1)

#     # 비밀번호 입력
#     try:
#         enter_keys(edit_pass, password)
#     except:
#         pass

#     # 인증비밀번호입력
#     try:
#         enter_keys(edit_cert, cert_password)
#     except:
#         pass

#     # 버튼 클릭
#     try:
#         click_button(button)
#     except:
#         pass


# def close_window(title, secs=5):
#     hwnd = find_window(title)
#     if hwnd !=0:
#         win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
#         time.sleep(secs)


# def execute_version_process():
#     try:
#         close_window("opstarter", secs=120)         # 버전처리 메시지 창이 있는 경우 120초 대기
#         close_window("업그레이드 확인")
#     except:
#         pass


# def close_login_window():
#     title = "Python 로그인"
#     try:
#         time.sleep(2)
#         close_window("계좌비밀번호")
#         close_window(title)
#         time.sleep(2)
#     except:
#         print("error: close login window")


# if __name__ == "__main__":
#     # 비밀번호
#     password = ""
#     cert_password = ""
#     password2 = ""

#     # 로그인 -> Auto 해제 -> 창닫기
#     open_login_window(password, cert_password)
#     set_auto_off()
#     close_login_window()

#     # 로그인
#     open_login_window(password, cert_password)
#     close_login_window()

#     # 버전처리 수행
#     execute_version_process()

#     # 로그인 -> Auto 재등록 -> 창닫기
#     open_login_window(password, cert_password)
#     set_auto_on(password2)
#     close_login_window()