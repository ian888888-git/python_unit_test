from typing import Union

class SignalProcessor:
    """Class Utility untuk membersihkan dan menghaluskan sinyal data sensor."""

    def __init__(self, window_size:int) -> None:
        """
        Inisialisasi konfigurasi ukuran jendela pemrosesan.
        Guard Clause: Mencegah ukuran window negatif atau nol.
        """
        if window_size <= 0:
            raise ValueError("Konfigurasi gagal! 'window_size' harus berupa bilangan bulat positif.")
        self.window_size = window_size

        def compute_moving_average(self, data_stream: list[Union[int, float]]) -> list[float]:
            """
            Menghitung nilai rata-rata bergerak menggunakan teknik Slicing Python.
            Parameter: data_stream: List data angka mentah dari sensor (1D List).
            Return: list[float]: List data baru yang sudah difilter/dihaluskan.
            """
            # Guard Clause: Jika jumlah data lapangan lebih sedikit dari ukuran window
            if len(data_stream) < self.window_size:
                return []
            
            smoothed_data: list[float] = []

            # Rumus batas perulangan agar index slicing tidak keluar batas (IndexError)
            total_steps = len(data_stream) - self.window_size + 1
            for i in range(total_steps):
                # Teknik Slicing: Mengambil potongan data dari indeks 'i' sepanjang 'window_size'
                current_window = data_stream[i:i+self.window_size]
                # Eksekusi Rumus Matematika Rata-rata
                average = sum(current_window)/self.window_size
                # Memastikan tipe data kembalian berupa float resmi standar industri
                smoothed_data.append(float(average))
            return smoothed_data
