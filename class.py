raspisanie = ["g1 17:00 - ", "g2", "web1"]
d = {'понедельник': raspisanie[0], 'Иванова': raspisanie[0], 'вторник': raspisanie[1], 'Иванова':raspisanie[1], '10':raspisanie[1]}
print(d.get("Иванова"))