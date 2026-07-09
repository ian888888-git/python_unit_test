from src.cleaner import DataCleaner
from src.metrics import MetricsCalculator
from src.transformer import DataTransformer
from src.signal_processor import SignalProcessor
from src.machine_anomaly_detector import MachineAnomalyDetector
from src.processors import SensorDataProcessor
from src.telemetry_monitor import TelemetryMonitor

class ProductionPipeline:
    def __init__(self) -> None:
        # Enkapsulasi objek helper ke dalam properti class pipeline
        self.cleaner = DataCleaner()
        self.metrics_manager = MetricsCalculator()
        self.transformer = DataTransformer()
        self.signal_processor = SignalProcessor(window_size=5)
        self.machine_anomaly_detector = MachineAnomalyDetector(z_treshold=3.0)
        self.processor = SensorDataProcessor(offset=2.0, default_value=20.0)
        self.telemetry_monitor = TelemetryMonitor(machine_id="M1", offset=2.0, default_value=20.0)
    
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
        
        # ----------------------------------------------------------------------
        # TAHAP 6: SENSOR DATA PROCESSOR 
        # ----------------------------------------------------------------------
        print("\n[6] Sensor Data Processor...")
        # 1. Inisialisasi processor dengan parameter kalibrasi mesin CNC 1
        process_cnc_temp = SensorDataProcessor(offset=2.5, default_value=20.0)
    
        # 2. Simulasi data streaming yang masuk dari hulu (CDC/Kafka)
        # Terdapat data normal, data ekstrem, dan data None (sensor sempat mati)
        raw_data_stream = [38.5, None, 41.2, 39.0, None]

        # 3. Kontainer untuk menampung data yang sudah bersih & siap dipakai
        clean_data_output = []
        for data in raw_data_stream:
            # Objek dipanggil langsung seperti fungsi berkat method __call__
            clean_value = process_cnc_temp(data)
            clean_data_output.append(clean_value)

        # ----------------------------------------------------------------------
        # TAHAP 7: TELEMETRY MONITOR 
        # ----------------------------------------------------------------------
        print("\n[7] Telemetry Monitor...")
        # 1. Menginisialisasi komponen monitor untuk 2 mesin berbeda di pabrik
        factory_monitor = [
            TelemetryMonitor(machine_id="CNC-01", offset=2.5),
            TelemetryMonitor(machine_id="CNC-02", offset=1.2, default_value=24.0)
        ]

        print("--- 1. Pengecekan Status via __str__ ---")
        for data_mesin in factory_monitor:
            print(data_mesin)
        
        print("\n--- 2. Eksekusi Aliran Data via __call__ ---")
        # Mengambil salah satu monitor untuk memproses data stream (ada data None/rusak)
        mesin_cnc_01 = factory_monitor[0]
        raw_data_stream = [39.0, None, 41.5]
        for raw_data in raw_data_stream:
            clean_data = mesin_cnc_01(raw_data) # Objek dieksekusi seperti fungsi biasa
            print(f"-> Raw Input: {raw_data}, Clear Output: {clean_data} °C")

        print("\n--- 3. Simulasi Log Kegagalan Cloud via __repr__ ---")
        # Jika List komponen dilempar ke sistem logging saat crash, __repr__ akan menyelamatkan Anda
        print(f"[CRITICAL ERROR LOG] Pipeline terhenti! Dump status komponen aktif:{factory_monitor} \n")
        print("\n=== [END] PIPELINE SELESAI DIALIRKAN DENGAN AMAN ===")
