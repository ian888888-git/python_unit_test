import re 
from typing import Union

class DataCleaner:
    """
    Sama seperti Class di PHP. Tempat mengumpulkan function-function utility.
    Di PHP biasanya kita sebut Utility Class atau Helper Class.
    """
    def clean_currency(self, value: Union[str, None]) -> int:
        """        
        - 'self' wajib ditulis di Python sebagai parameter pertama, fungsinya sama dengan $this di PHP.
        - value: Union[str, None] Ini disebut Type Hinting (penanda tipe data) untuk argumen bernama value
        - 'Union[str, None]' Artinya, variabel value ini hanya boleh berisi teks (str) ATAU kosong.
        - '-> int' adalah return type, memaksa function ini mengembalikan integer.
        """
        # Cek isset/is_null. Jika input kosong, langsung hentikan fungsi dan return 0.
        if value is None: 
            return 0
        
        # Eksekusi regex preg_replace. Menghapus semua karakter kecuali digit angka (0-9).
        cleaned_str = re.sub(r'[^\d]','', value)

        # Cek empty string. Jika setelah dibersihkan string menjadi kosong, return 0.
        if not cleaned_str:
            return 0
        
        # Type casting string angka menjadi tipe data Integer resmi. Sama seperti (int)$cleaned_str di PHP.
        return int(cleaned_str)
    
    def validated_sensor_temp(self, temp: Union[int, float, None]) -> float:
        """        
        - 'self' bertindak sebagai pointer ke instance class saat ini ($this).
        - 'temp: Union[int, float, None]' Argumen temp menerima input bertipe Integer, Float, atau Kosong (Null).
        - '-> float' Memaksa function ini wajib mengembalikan data bertipe desimal (Float).
        """
        # Validasi jika parameter tidak diisi atau bernilai Null. Jika ya, lempar Exception.
        if temp is None:
            raise ValueError("Data suhu tidak boleh kosong (None).")

        # Type casting input menjadi Float agar format data seragam untuk kalkulasi.
        current_temp = float(temp)

        # Validasi batasan angka. Jika kondisi terpenuhi, lempar Exception (ValueError).
        if current_temp > 150.0:
            raise ValueError(f"Anomali Terdeteksi! Suhu ekstrem: {current_temp}°C. Maksimal batas aman 150°C.") 
        
        # Mengembalikan nilai yang lolos pengecekan.
        return current_temp
