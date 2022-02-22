nasabah = {
      'nama':'Rei',
      'pin': 1234,
      'saldo':1000
}


def cek_login():
      fail = 0
      while True:
            password = int(input('Masukkan pin anda : '))
            if password != nasabah['pin']:
                  fail += 1
                  if fail <= 4:
                        print('Pin salah ulangi!')
                  if fail == 5:
                        print('Coba lagi nanti')
                        break
                        
            else:
                  print('Selamat datang', nasabah['nama'])
                  break
cek_login()    

def menu():
      print('Apa yang ingin anda lakukan?')
      print('1.Cek Saldo')
      print('2.Isi Saldo')
      print('3.Tarik Saldo')
      print('4.Transfer')
      jwb = int(input('Masukkan pilihan anda : '))
      if jwb == 1:
            print('Saldo anda sekarang : ', nasabah['saldo'])

      elif jwb == 2: 
            jml = int(input('Masukkan jumlah uang anda :'))
            nasabah['saldo'] = nasabah['saldo'] + jml
            print('Jumlah saldo sekarang :', nasabah['saldo'])

      elif jwb == 3:
            jml = int(input('Masukkan jumlah uang :'))
            nasabah['saldo'] = nasabah['saldo'] - jml
            if jml >= nasabah['saldo']:
                  print('Penarikan terlalu besar saldo tidak cukup')
            else:
                  print('Saldo anda sekarang tersisa :', nasabah['saldo'])    
      
      elif jwb == 4:
            print('Sedang tahap pengembangan')
      
      else:
            print('Input anda salah ulangi')
            menu()

      while True:
            lagi = 'y'
            lagi2 = input('Apakah anda ingin mengulanginya lagi? y/n : ')
            if lagi2 == lagi:
                  menu()      
            else:
                  print('Terimakasih')
                  break
  menu()  
