from src.cleaner import DataCleaner
from src.cleaner import MetricsCalculator

class ProductionPipeline:
    def __self__(self) -> None:
        # Enkapsulasi objek helper ke dalam properti class pipeline
        self.cleaner = DataCleaner()
        self.metrics_manager = MetricsCalculator
    
    def start(self) -> None:
        print("\n=== [START] MEMULAI AUTOMATED DATA PIPELINE ===")

        # ----------------------------------------------------------------------
        # TAHAP 1: EKSEKUSI DATA CLEANER (Menggunakan Fungsi Asli Anda)
        # ----------------------------------------------------------------------
        print("[1] Menjalankan Modul Pembersihan Data Teks & Sensor...")
        
        # Eksekusi fungsi pertama: clean_currency
        raw_salary = "Rp 12.500.000,00"
        clean_salary = self.cleaner.clean_currency(raw_salary)
        print(f"->Input Gaji {raw_salary} -> Hasil Casting Integer: {clean_salary}")

        # Eksekusi fungsi kedua: validated_sensor_temp
        raw_temp = 42.5 
        validated_temp = self.cleaner.validated_sensor_temp(raw_temp)
        print(f"->Input Suhu {raw_temp} -> Hasil Casting Float: {validated_temp}°C")

        # ----------------------------------------------------------------------
        # TAHAP 2: EVALUASI METRIK PIPELINE (Sesuai Fungsi asli evaluates_record)
        # ----------------------------------------------------------------------
        print("\n[2] Mengevaluasi Metrik Kualitas Ekosistem Data...")
        # Mengirimkan parameter sesuai spesifikasi fungsi asli Anda
        # Simulasi: 1000 total data, 960 data valid (Akurasi 96.0% -> Lolos Threshold 95%)
        message, score, ml_status = self.metrics_manager.evaluates_record(
            total_records=1000,
            valid_records=980,
            component_name="automated_sensor_08"
        )
        # Unpacking nilai tuple hasil kembalian dari metrics.py
        print(f"-> Log Status: {message}")
        print(f"-> Skor Akurasi: {score}%")
        print(f"-> Status ML: {"LOLOS TRESHOLD 95%" if ml_status else "BUTUH REVISI"}")
        print("\n=== [END] PIPELINE SELESAI DIALIRKAN DENGAN AMAN ===")
