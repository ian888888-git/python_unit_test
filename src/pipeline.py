from src.cleaner import DataCleaner
from src.metrics import MetricsCalculator
from src.transformer import DataTransformer
from src.signal_processor import SignalProcessor
from src.machine_anomaly_detector import MachineAnomalyDetector

class ProductionPipeline:
    def __init__(self) -> None:
        # Enkapsulasi objek helper ke dalam properti class pipeline
        self.cleaner = DataCleaner()
        self.metrics_manager = MetricsCalculator()
        self.transformer = DataTransformer()
        self.signal_processor = SignalProcessor(window_size=5)
        self.machine_anomaly_detector = MachineAnomalyDetector(z_treshold=3.0)
    
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
        print(f"-> Status ML: {'LOLOS TRESHOLD 95%' if ml_status else 'BUTUH REVISI'}")

        # ----------------------------------------------------------------------
        # TAHAP 3: MENJALANKAN TRANSFORMASI DATA
        # ----------------------------------------------------------------------
        print("\n[3] Operasi Transformasi Matrix 2D...")
        raw_data = [0.95, 0.92, 0.88, 0.91, 0.94, 0.89]
        dimensions = (3,2)
        try:
            structured_matrix = self.transformer.reshape_matrix(raw_data, dimensions)
            print(f"-> Sukses Matrix 2D {dimensions[0]}x{dimensions[1]}:")
            for row in structured_matrix:
                print(row)
        except ValueError as e:
            print(f"-> Terjadi Masalah Transformasi: {e}")
        
        # ----------------------------------------------------------------------
        # TAHAP 4: SIGNAL PRCESSOR
        # ----------------------------------------------------------------------
        print("\n[4] Operasi Signal Processor...")
        raw_sensor_data = [20, 24, 22, 28, 26]
        try:
            signal_result = self.signal_processor.compute_moving_average(raw_sensor_data)
            print(f"-> Hasil rata-rata: {signal_result}")
        except ValueError as e:
            print(f"-> Terjadi Masalah Signal Processor: {e}")    
        
        # ----------------------------------------------------------------------
        # TAHAP 5: ANOMAL MACHINE 
        # ----------------------------------------------------------------------
        print("\n[5] Deteksi Anomaly Machine...")
        history_data = [70, 72, 68, 74] # Rata-rata 71, Deviasi 2.23
        current_value = 93 # Nilai diatas batas toleransi
        try:
            anomaly_result = self.machine_anomaly_detector.is_machine_anomaly(current_value, history_data)
            print(f"-> Hasil Deteksi Anomaly: {'TERDETEKSI' if anomaly_result else 'TIDAK TERDETEKSI'}")
        except ValueError as e:
            print(f"-> Terjadi Masalah Anomaly Machine: {e}")
        print("\n=== [END] PIPELINE SELESAI DIALIRKAN DENGAN AMAN ===")
