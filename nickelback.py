songs = {
  ('Nickelback', 'How You Remind Me'),
  ('Creed', 'Higher'),
  ('Nickelback', 'Figured You Out'),
  ('Creed', 'Arms Wide Open'),
  ('3 Doors Down', 'Kryptonite'),
  ('3 Doors Down', 'Here Without You')
}


non_nickelback_songs = {song[1] for song in songs if song[0] != 'Nickelback'}

print(non_nickelback_songs)