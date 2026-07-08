import pytest 
from src.signal_processor import SignalProcessor

class TestSignalProcessor:
    def test_compute_moving_average_success(self) -> None:
        """
        Memastikan perhitungan rata-rata bergerak berjalan akurat pada kondisi normal.
        Setup data tiruan sensor (misal data suhu mesin)
        """
        raw_sensor_data = [20, 24, 22, 28, 26]
        windows_size = 3
        processor = SignalProcessor(windows_size)

        # Eksekusi fungsi
        result = processor.compute_moving_average(raw_sensor_data)
        # Ekspektasi Hasil: 
        # Jendela 1: (20+24+22)/3 = 22.0
        # Jendela 2: (24+22+28)/3 = 24.666...
        # Jendela 3: (22+28+26)/3 = 25.333...
        expected_result == [22.0, 24.666666666666668, 25.333333333333336] # type: ignore

        # Validasi Assert
        assert len(result) == 3
        # Menggunakan pytest.approx untuk mengantisipasi selisih angka desimal (floating point)
        assert result == pytest.approx(expected_result) # type: ignore
    
    def test_compute_moving_average_short_data(self) -> None:
        """Memastikan perhitungan rata-rata bergerak berjalan akurat pada kondisi data lapangan terlalu pendek."""
        raw_sensor_data = [10, 12]
        windows_size = 5
        processor = SignalProcessor(windows_size)
        result = processor.compute_moving_average(raw_sensor_data)
        # Ekspektasi: Lolos Guard Clause dan menghasilkan list kosong tanpa error
        assert result == []

    def test_invalid_windows_size_raises_error(self) -> None:
        """Memastikan sistem pengaman melempar ValueError jika konfigurasi window tidak valid (<= 0)."""
        invalid_windows = 0
        # Penguji harus menangkap ledakan ValueError dari constructor __init__
        with pytest.raises(ValueError) as exc_info:
            SignalProcessor(invalid_windows)
        
        # Memastikan pesan alarm pengaman sesuai
        assert "Konfigurasi gagal! 'window_size' harus berupa bilangan bulat positif." in str(exc_info.value)

