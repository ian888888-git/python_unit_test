import pytest 
from src.processors import SensorDataProcessor

def test_sensor_processor_is_callable():
    """Memastikan objek memenuhi arsitektur standar sebagai Callable Object."""
    processor = SensorDataProcessor(offset=2.0)
    # Menguji apakah objek bisa dieksekusi langsung dengan tanda kurung ()
    assert callable(processor) == True, "Gagal: Objek harus memiliki method __call__!" 

def test_sensor_processor_normal():
    """Memastikan kalkulasi matematika ETL berjalan dengan data normal."""
    processor = SensorDataProcessor(offset=1.5, default_value=0.0)
    # Hasil harusnya: 40.0 + 1.5 = 41.5
    assert processor(40.0) == 41.5

def test_sensor_processor_none():
    """Memastikan Guard Clause bekerja jika menerima data None (tidak crash)."""
    processor = SensorDataProcessor(offset=1.5, default_value=20.0)
    # Hasil jika None: ambil default_fill (20.0) -> tambahkan offset (1.5) = 21.5
    assert processor(None) == 21.5
