from typing import Union, List

class DataTransformer():
    def reshape_matrix(self, raw_list: List[Union[int, float]], dimensions: tuple[int, int]) -> list[list[float]]:
        """
        Mengubah flat list (1 dimensi) menjadi matriks 2 dimensi (list di dalam list).
        Parameter:
        - raw_list: List berisi angka desimal atau integer.
        - dimensions: Tuple berisi (jumlah_baris, jumlah_kolom).
        """
        rows, cols = dimensions
        # VALIDATION GUARD: Jika perkalian dimensi tidak sesuai dengan total elemen
        if rows * cols != len(raw_list):
            raise ValueError(
                f"Kesalahan Dimensi! Dimensi {rows}x{cols} membutuhkan {rows * cols} elements,"
                f"tetapi data mentah hanya menyediakan {len(raw_list)} elements."
            )

        # Proses transformasi menggunakan teknik Slicing Python
        matrix_result = []
        for i in range(rows):
            start_index = i * cols
            end_index = start_index + cols 
            # Ambil potongan list sepanjang ukuran kolom, ubah elemen ke float resmi
            row_data = [float(item) for item  in raw_list[start_index:end_index]]
            matrix_result.append(row_data)
        return matrix_result
    
