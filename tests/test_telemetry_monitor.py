import pytest
from src.telemetry_monitor import TelemetryMonitor

class TestTelemetryMonitor:
    def test_monitor_is_callable(self,):
        """Memastikan objek dapat dipanggil langsung (memiliki __call__)."""
        monitor = TelemetryMonitor(machine_id="TEST-01", offset=0.0)
        assert callable(monitor) == True, "Gagal: Objek harus memiliki method __call__!"

    def test_monitor_math_calculation(self):
        """Memastikan proses pembersihan dan kalibrasi matematika akurat."""
        monitor = TelemetryMonitor(machine_id="TEST-01", offset=1.5, default_value=20.0)
        assert monitor(40.0) == 41.5
        assert monitor(None) == 21.5
    
    def test_monitor_representation(self):
        """Memastikan format cetakan teks log tidak berubah dan terkunci."""
        monitor =  TelemetryMonitor(machine_id="CNC-01", offset=3.0, default_value=5.0)
        assert str(monitor) == "Telematri Monitor Aktif -> Mesin ID: CNC-01"
        assert repr(monitor) == "TelemetryMonitor(machine_id='CNC-01', offset=3.0, default_value=5.0)"