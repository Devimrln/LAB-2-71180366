'''
Tina dan Rena memiliki motor masing-masing dengan tipe 
motor Revo 110 F1 dan beat eSP, masing-masing jika di isi 
bahan bakar full 4.5 liter dan 4 liter. 
Mereka berencana untuk pergi ke kota S menggunakan motor
dengan titik start dari rumah tina berjarak 63.4 Km. 
berapa konsumsi bahan bakar motor mereka dalam 1 liter 
bensin dapat berjalan sejauh?
'''
#input
Revo = 4.5 #liter
Beat = 4 #liter
jarak = 63.4 #km

#proses
#Rumus = jarak / liter bensin
konsumsiRevo = jarak / Revo
konsumsiBeat = jarak / Beat

#output
print("Jadi konsumsi bahan bakar Revo 110 F1 ialah 1 liter bensin sejauh %.2f " % konsumsiRevo, "Km/l")
print("sedangkan konsumsi bahan bakar beat eSP ialah 1 liter bensin sejauh %.2f " % konsumsiBeat, "Km/l")