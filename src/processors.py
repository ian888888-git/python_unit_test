class SensorDataProcessor:
    def __init__(self, offset: float, default_value: float = 0.0) -> None:
        """
        Inisialisasi konfigurasi komponen ETL.
        """
        self.offset = offset 
        self.default_value = default_value
    
    def _clean_missing_value(self, value: float | None) -> float:
        """Fungsi Internal 1: Menangani data kosong (Imputation)."""
        if value is None:
            return self.default_value
        return value
    
    def _scale_temperature(self, value: float) -> float:
        """Fungsi Internal 2: Melakukan kalibrasi matematika skala data."""
        return value + self.offset
    
    def log_transformation(self, raw: float | None, result: float) -> None:
        """Fungsi Internal 3: Pelapor status transformasi data (Auditor)."""
        print(f"-> [LOG ETL] Sukses Transformasi: {raw} -> {result}°C") 
    
    def __call__(self, raw_data: float | None) -> float:
        """
        Gerbang Utama (Main Entry Point): Merajut seluruh fungsi internal
        menjadi satu kesatuan aliran ban berjalan (pipeline).
        """
        step_1 = self._clean_missing_value(raw_data)
        step_2 = self._scale_temperature(step_1)
        self.log_transformation(raw_data, step_2) # Auditor (Log ETL)
        return step_2