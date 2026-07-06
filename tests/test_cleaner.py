import pytest 
from src.cleaner import DataCleaner

class TestDataCleaner:
    """
    Class Test Suite untuk pengujian otomatis. 
    Menggunakan framework pytest untuk menggantikan kebiasaan var_dump() secara manual.
    """
    @pytest.fixture(autouse=True)
    def setup(self):
        """        
        - '@pytest.fixture(autouse=True)' Adalah Decorator. Fungsinya memaksa method ini berjalan otomatis paling awal.
        - Ini sama persis dengan method protected function setUp(): void di PHPUnit.
        - Berguna untuk instansiasi object secara global sebelum tiap fungsi tes dieksekusi.
        """
        # Menyimpan instance DataCleaner ke properti object. Sama seperti $this->cleaner = new DataCleaner();
        self.cleaner = DataCleaner()
    def test_clean_currency_normal(self):
        """        
        - Fungsi pengujian wajib diawali dengan prefix nama 'test_'. Jika tidak, pytest tidak akan mendeteksinya.
        - 'assert' Adalah perintah pengujian inti. Jika kondisi bernilai True, tes lulus. Jika False, tes gagal.
        """
        assert self.cleaner.clean_currency("Rp 50.000") == 50000
        assert self.cleaner.clean_currency("RP. 1.250.000") == 1250000

    def test_clean_currency_none_and_empty(self):
        """        
        - Menguji performa fungsi saat menangani data bermasalah (Edge Case).
        - Memastikan sistem mengembalikan angka 0 dan tidak memicu fatal error/crash saat menerima data Null.
        """
        assert self.cleaner.clean_currency(None) == 0
        assert self.cleaner.clean_currency("RP -") == 0 
        assert self.cleaner.clean_currency("") == 0
    
    def test_validate_sensor_temp_normal(self):
        """        
        - Memasukkan parameter uji normal berupa float asli dan string berisi angka desimal.
        - Memastikan sistem melakukan casting dengan benar dan meloloskan data tersebut.
        """
        assert self.cleaner.validated_sensor_temp(120.5) == 120.5
        assert self.cleaner.validated_sensor_temp("98") == 98.0
        assert self.cleaner.validated_sensor_temp("88.88") == 88.88
    
    def test_validate_sensor_temp_extreme_raises_error(self):
        """        
        - 'with pytest.raises(ValueError) as exc_info' Bertindak seperti blok try-catch untuk menangkap Exception.
        - Tes ini dinyatakan LULUS justru jika fungsi di dalamnya sukses memicu Exception ValueError.
        - 'exc_info' Menyimpan objek error yang tertangkap untuk diperiksa teks pesannya secara spesifik.
        """
        with pytest.raises(ValueError) as exc_info:
            self.cleaner.validated_sensor_temp(155.3)
            # Memastikan string pesan di dalam Exception mengandung frasa tertentu (strpos / str_contains di PHP).
            assert "Anomali Terdeteksi" in str(exc_info.value)
    
    def test_validate_sensor_temp_none_raises_error(self):
        """        
        - Membuka blok penangkap Exception untuk memastikan input Null (None) ditolak oleh sistem.
        """
        with pytest.raises(ValueError):
            self.cleaner.validated_sensor_temp(None)