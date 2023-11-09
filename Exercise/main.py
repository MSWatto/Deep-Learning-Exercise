from pattern import checker, circle
resolution=int(input('Enter the resolution: '))
tile_size=int(input('Enter size of the boxes you want: '))
chk_game=checker(resolution,tile_size)
chk_game.show()