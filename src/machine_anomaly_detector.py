import math
from typing import Union

class MachineAnomalyDetector:
    """Class standar industri untuk mendeteksi anomali dinamis pada mesin manufaktur."""
    def __init__(self, z_treshold: float = 3.0) -> None:
        """Inisialisasi batas toleransi statistik dinamis (Standard: Rule 3-Sigma)."""
        if z_treshold <= 0:
            raise ValueError("Konfigurasi gagal! 'z_threshold' harus bernilai positif.")
        self.z_treshold = z_treshold
    
    def is_machine_anomaly(self, current_value: Union[int, float], history_data: list[Union[int, float]]) -> bool:
        """
        Mengecek apakah hasil pembacaan sensor mesin terbaru (current_reading) 
        mengalami lonjakan tidak wajar dibanding data historisnya.
        """
        # Guard Clause 1: Jika data historis kurang dari 2, perhitungan statistik dibatalkan
        if len(history_data) < 2:
            return False
        # 1. Hitung Nilai Miu (Mean / Rata-rata suhu historis mesin)
        mean = sum(history_data) / len(history_data)
        # 2. Hitung Nilai Variance (Varians / Rata-rata kuadrat jarak internal mesin)
        variance = sum((x - mean) ** 2 for x in history_data) / len(history_data)
        # Hitung Nilai Sigma (Standar Deviasi / Batas toleransi fluktuasi fisik mesin)
        std_dev = math.sqrt(variance)
        # Guard Clause 2: Jika data mesin kembar semua, deviasi 0 diisolasi agar tidak crash
        if std_dev == 0:
            return False
        # 3. Hitung Nilai Z-Score untuk pembacaan sensor saat ini
        z_score = (current_value - mean) / std_dev
        # 4. Evaluasi Akhir: Apakah nilai mutlak Z-Score mendobrak batas toleransi mesin?
        return abs(z_score) > self.z_treshold