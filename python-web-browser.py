import webbrowser
import time

chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
# webbrowser.get('chrome').open_new_tab("google.com")
chap_start = 2234
chap_end = 2350

for i in range(chap_start,chap_end):
    webbrowser.get('chrome').open_new_tab(
        "https://truyencv.com/van-co-than-de/chuong-{}/".format(i)
    )
    time.sleep(2)
