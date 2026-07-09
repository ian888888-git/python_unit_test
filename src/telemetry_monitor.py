class TelemetryMonitor:
    def __init__(self, machine_id: str, offset: float, default_value: float = 0.0):
        """
        Inisialisasi konfigurasi komponen ETL Telemetri Mesin.
        """
        self.machine_id = machine_id
        self.offset = offset
        self.default_value = default_value
    
    def _clean_missing_value(self, value: float | None) -> float:
        """Fungsi Internal 1: Mengisi data kosong (None) dengan nilai aman."""
        if value is None:
            return self.default_value
        return value

    def _scale_temperature(self, value: float) -> float:
        """Fungsi Internal 2: Kalibrasi matematika skala data suhu."""
        return value + self.offset
    
    def __call__(self, raw_data: float | None) -> float:
        """
        Gerbang Utama (Materi 1): Mengalirkan data melewati stasiun pembersihan 
        dan kalibrasi secara otomatis saat objek dipanggil.
        """
        step_1 = self._clean_missing_value(raw_data)
        step_2 = self._scale_temperature(step_1)
        return step_2
    
    def __str__(self) -> str:
        """Materi 2: Tampilan teks ramah untuk operator / dashboard produksi."""
        return f"Telematri Monitor Aktif -> Mesin ID: {self.machine_id}"
    
    def __repr__(self) -> str:
        """Materi 2: Dokumen parameter internal untuk kebutuhan log error di server cloud."""
        return(f"CncTelemetryMonitor(machine_id={self.machine_id}," f"offset={self.offset}," f"default_value={self.default_value})")