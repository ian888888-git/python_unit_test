class MetricsCalculator:
    """Class khusus untuk menghitung metrik kualitas data dalam pipeline MLOps."""

    def evaluates_record(self, total_records: int, valid_records: int, component_name: str) -> tuple[str, float, bool]:
        """
        Fungsi ini digunakan untuk menghitung metrik kualitas data dalam pipeline MLOps.
        Menerima lebih dari satu parameter untuk mengevaluasi kualitas data.

        Mengembalikan 3 nilai (Tuple):
        - Status ringkasan (str)
        - Persentase akurasi data (float)
        - Keputusan kelayakan untuk masuk ke model ML (bool)
        """
        # Proteksi pembagian dengan angka nol
        if total_records <= 0:
            return f"Komponen [{component_name}]: Gagal: Total data tidak boleh nol atau negatif.", 0.0, False
        
        # 1. Hitung persentase data yang valid
        accuracy_score = round((valid_records/total_records) * 100, 2)

        # 2. Tentukan keputusan kelayakan (Threshold industri: 95% valid)
        is_ready_for_ml = accuracy_score >= 95.0 

        # 3. Buat ringkasan status teks
        status_summary = f"SUKSES" if is_ready_for_ml else f"Gagal: Butuh Revisi - Akurasi data {accuracy_score}% di bawah threshold 95%."
        final_message = f"[{component_name.upper()}] Status: {status_summary} dengan score {accuracy_score}%"

        return final_message, accuracy_score, is_ready_for_ml
