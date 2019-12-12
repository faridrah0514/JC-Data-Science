import datetime as dt

class waktu_lengkap:
    hari_dictionary={
        'Monday': 'Senin',
        'Tuesday': 'Selasa',
        'Wednesday': 'Rabu',
        'Thursday': 'Kamis',
        'Friday': 'Jumat',
        'Saturday': 'Sabtu',
        'Sunday': 'Minggu'
    }

    k=dt.datetime.now()
    def __init__(self):
        self.hari = self.hari_dictionary[self.k.strftime('%A')]
        self.tanggal = self.k.strftime('%d')
        self.bulan = self.k.strftime('%B')
        self.tahun = self.k.strftime('%Y')
        self.jam = self.k.strftime('%H')
        self.menit = self.k.strftime('%M')
        self.detik = self.k.strftime('%S')