time = input("Введите время в секундах: ")
time = int(time)
hh = time // 3600
mm = (time // 60) - (hh * 60)
ss = time % 60
print("Время в формате ЧЧ:ММ:СС %02d:%02d:%02d" % (hh, mm, ss))
print("Время в формате ЧЧ:ММ:CC {:02}:{:02}:{:02}".format(hh, mm, ss))
print(f"Время в формате ЧЧ:ММ:CC {hh:02}:{mm:02}:{ss:02}")
