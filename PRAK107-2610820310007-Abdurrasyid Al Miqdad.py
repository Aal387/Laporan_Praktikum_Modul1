import math

putaran = 5
jarak = 14

jari_jari = jarak / (putaran * 2 * math.pi)

print("Diketahui : Pak Dengklek mengelilingi taman =", putaran, "Putaran")
print("Jarak tempuh Pak Dengklek =", jarak, "Kilometer")
print("Jawaban :")
print("Jari-jari taman yang dikelilingi Pak Dengklek adalah {:.2f} Kilometer".format(jari_jari))