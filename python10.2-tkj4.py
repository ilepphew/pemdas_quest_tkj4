# membuat tipe data koleksi

koleksi_data_str = ["pisang", "mangga", "jambu", "semangka"]

koleksi_data_int = [200, 300, 400, 500]

koleksi_data_mix = ["rizky billar", 100, True, "reza arap"]

print("koleksi data string:", koleksi_data_str)

print("koleksi data integer:", koleksi_data_int)

print("koleksi data campuran:", koleksi_data_mix)

# buatlah 3 kumpulan data : nama hewan, nilai uts, nama teman sebangku  kalian

koleksi_data_pribadi = ["burung hantu", 92, "lulu", "panda", 86, "dewi", "beruang", 96]

nama_hewan = ["panda", "burung hantu", "beruang"]

nama_nilai = [100, 90, 86, 96]

nama_teman = ["nazla", "lev", "lulu dan dewi"]

print("koleksi data pribadi:", koleksi_data_pribadi)

# tampilkan data koleksi dengan indeks

print("data pertama nama hewan", nama_hewan[0])

# data kedua nama hewan

print("data kedua nama hewan adalah", nama_hewan[1])

# data pertama nilai uts

print("data pertama nilai uts adalah", nama_nilai[0])

# data ketiga nama teman sebangku

print("data terakhir teman sebangku adalah", nama_teman[2])

# tambahkan 1 data di setiap data koleksi

nama_hewan.append("koala")

nama_nilai.append("90")

nama_teman.append("diaana")

print(nama_hewan, nama_nilai, nama_teman)

# ubahlah data terakhir nilai uts

nama_nilai[-1] = 50

# ubahlah data ketiga nama hewan

nama_hewan[2] = "kelinci"

print(nama_nilai, nama_hewan)