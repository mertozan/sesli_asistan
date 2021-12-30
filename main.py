import sys
import speech_recognition as sr
import webbrowser
import time
import locale
import subprocess
import pyautogui
import requests
import json
import gtts
import os
import random
from playsound import playsound
from pynput.keyboard import Key,Controller
keyboard = Controller()
locale.setlocale(locale.LC_TIME, "tr_TR")


def listen(kaynak, timeout):
    voice = r.listen(kaynak, phrase_time_limit=timeout)
    try:
        return r.recognize_google(voice, language="tr-TR")
    except sr.UnknownValueError:
        print("Anlamadım")
    except sr.RequestError:
        print("Bad Request")


def speak(text):
    print(text)
    tts = gtts.gTTS(text, lang="tr")
    r1 = random.randint(1, 10000000)
    r2 = random.randint(1, 10000000)
    randfile = str(r2) + "randomtext" + str(r1) + ".mp3"
    tts.save(randfile)
    playsound(randfile)
    os.remove(randfile)

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:

        speak("Merhaba nasıl yardımcı olabilirim?")
        command = listen(source, None)
        print(command)
        if command == "ara":
            speak("Ne aramak istiyorsunuz ?")
            second_command = listen(source, 2)
            print(second_command)
            webbrowser.open('https://www.google.com/search?q=' + second_command, new=2)
        elif command == "tarih":
            print( time.strftime("%a, %d %b %Y %H:%M:%S"))
        elif command == "ses ayarları":
            while True:
                speak("Sesi kısmak için 'Azalt', arttırmak için 'Arttır',çıkmak için 'Çık' komutunu verin")
                second_command = listen(source, 1)
                print(second_command)
                if second_command == "azalt":
                    for i in range(10):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)
                        time.sleep(0.1)
                    speak("Ses azaltıldı")
                elif second_command == "arttır":
                    for i in range(10):
                        keyboard.press(Key.media_volume_up)
                        keyboard.release(Key.media_volume_up)
                        time.sleep(0.1)
                    speak("Ses arttırıldı")
                elif second_command == "çık":
                    break
                else:
                    speak("Yanlış komut girdiniz 'Arttır' veya 'Azalt' söyleyin")
        elif command == "program aç":
            speak("Hangi programı açmak istiyorsunuz?")
            second_command = listen(source, 1)
            print(second_command)
            if second_command == "belge":
                subprocess.Popen('C:\Windows\System32\write.exe')
            elif second_command == "hesap makinesi":
                subprocess.Popen('C:\Windows\System32\calc.exe')
            elif second_command == "görev yöneticisi":
                subprocess.Popen('C:\Windows\System32\Taskmgr.exe')
            elif second_command == "denetim masası":
                subprocess.Popen('C:\Windows\System32\control.exe')
            elif second_command == "web tarayıcı":
                subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe')

        elif command == "fare ayarları":
            while True:
                speak("Fare moduna geçildi, komutlarınızı söyleyiniz")
                second_command = listen(source, 1)
                print(second_command)
                if second_command == "yukarı":
                    pyautogui.moveRel(0, -100, duration=0)
                elif second_command == "aşağı":
                    pyautogui.moveRel(0, 100, duration=0)
                elif second_command == "Sağ":
                    pyautogui.moveRel(100, 0, duration=0)
                elif second_command == "sola":
                    pyautogui.moveRel(-100, 0, duration=0)
                elif second_command == "tıkla":
                    pyautogui.click()
                elif second_command == "çift tıkla":
                    pyautogui.doubleClick()
                elif second_command == "yukarı kaydır":
                    pyautogui.scroll(200)
                elif second_command == "aşağı kaydır":
                    pyautogui.scroll(-200)
                elif second_command == "sağa tıkla":
                    pyautogui.rightClick()
                elif second_command == "çık" or "çıkış yap":
                    break
                else:
                    speak("Anlayamadım")

        elif command == "ekran görüntüsü":
            keyboard.press(Key.print_screen)
            keyboard.release(Key.print_screen)
            time.sleep(0.1)

        elif command == "klavye ayarları":
            speak("Yapılacak işlemi söyleyin")
            second_command = listen(source, 1)
            print(second_command)
            if second_command == "giriş":
                pyautogui.press('enter')
            elif second_command == "yazdır":
                speak("Yazdırılacak şeyi söyleyin")
                third_command = listen(source, 1)
                print(third_command)
                pyautogui.write(third_command)

        elif command == "hava durumu":
            speak("Hangi şehrin hava durumunu öğrenmek istiyorsunuz?")
            second_command = listen(source, 1)
            r = requests.get('https://wttr.in/' + second_command + "?format=j1")
            response = r.json()
            print("Normal sıcaklık :", response["current_condition"][0]["temp_C"])
            print("Hissedilen sıcaklık :", response["current_condition"][0]["temp_C"])

        elif command == "asistan'ı kapat" or "asistanı kapat" or "kapat":
            speak("Program kapatılıyor...")
            sys.exit()
        elif command is None:
            speak("Anlayamadım")
