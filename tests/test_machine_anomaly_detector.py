import pytest
from src.anomaly_detector import MachineAnomalyDetector

class TestMachineAnomalyDetector: 
    # Testing konfigurasi z_treshold tidak bernilai negatif
    def test_invalid_z_treshold(self) -> None: 
        with pytest.raises(ValueError) as exc_info: 
            MachineAnomalyDetector(-1.5)
        assert "Konfigurasi gagal! 'z_threshold' harus bernilai positif." in str(exc_info.value)
    
    # Testing Insufisien History Data  
    def test_insufficient_history_data(self) -> None:
        """Memastikan sistem langsung mengembalikan False jika data sensor masa lalu belum cukup."""
        detector = MachineAnomalyDetector(z_treshold=3.0) 
        history_data = [70]
        current_value = 80
        result = detector.is_machine_anomaly(current_value, history_data)
        assert result is False
    
    # Testing Deteksi Anomaly | Machine Normal - FALSE 
    def test_is_machine_normal(self) -> None:
        """Memastikan sensor membaca kondisi normal saat suhu mesin berfluktuasi wajar."""
        detector = MachineAnomalyDetector(z_treshold=3.0)
        history_data = [70, 72, 68, 74] # Rata-rata 71, Deviasi 2.23
        current_value = 73 # Nilai diatas rata-rata
        result = detector.is_machine_anomaly(current_value, history_data)
        assert result is False
    
    # Testing Deteksi Anomaly | Machine Anomaly - TRUE 
    def test_is_machine_anomaly(self) -> None:
        """Memastikan alarm berbunyi (True) saat terjadi lonjakan suhu ekstrem akibat kerusakan."""
        detector = MachineAnomalyDetector(z_treshold=3.0)
        history_data = [70, 72, 68, 74] # Rata-rata 71, Deviasi 2.23
        current_value = 93 # Nilai diatas batas toleransi
        result = detector.is_machine_anomaly(current_value, history_data)
        assert result is True