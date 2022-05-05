import libtorrent
import os

info = libtorrent.torrent_info('torrent/source.torrent')
index = 0
max_index = len(info.files())

for file in info.files():
    print("[%s] - %s" % (index, file.path))
    index += 1

while True:
    episode_selection = int(input("Vyberte si díl SpongeBoba: "))

    while episode_selection > max_index or episode_selection < 0:
        episode_selection = input("Zadejte díl znovu, zadal jste neexistující díl: ")

    os.system("webtorrent torrent/source.torrent -s %s --vlc --player-args='--fullscreen'" % episode_selection)

