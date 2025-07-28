import time
import sys
import os

os.system('clear')

lyrics = [
    (0.0, "Chỉ cần ai đó cạnh bên dừng lại..."),
    (4.0, "\tvà níu lấy em chỉ một phút giây"),
    (8.2, "Dù là có đúng hay sai"),
    (11.0, "Vẫn cứ yêu thêm một lần"),
    (11.0, "\tchẳng cần nghi ngại"),
    (15.0, "Ngày dài vẫn thế cứ thế trôi hoài"),
    (19.0, "Lạc mất nhau sao mình còn đi mãi"),
    (22.5, "Nơi anh đến sẽ là..."),
    (25.0, "Một nơi chẳng còn có anh")
]

start_time = time.time()
for i, (timestamp, lyric) in enumerate(lyrics):
    while time.time() - start_time < timestamp:
        time.sleep(0.1)
    for ch in lyric:
        print(ch, end='', flush=True)
        time.sleep(0.1)
    print()
