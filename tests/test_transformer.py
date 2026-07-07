import pytest 
from src.transformer import DataTransformer

class TestDataTransformer: 
    @pytest.fixture(autouse=True) 
    def setup(self):
        self.transformer = DataTransformer() 
    
    def test_reshape_matrix_success(self) -> None:
        """Memastikan transformasi flat list menjadi matriks 2D berjalan sukses."""
        raw_data = [1,2,3,4]
        dimensions = (2,2) 
        result = self.transformer.reshape_matrix(raw_data, dimensions)

        # Ekspektasi: [[1.0, 2.0], [3.0, 4.0]]
        assert len(result) == 2 #Memiliki 2 baris 
        assert len(result[0]) == 2 #Memiliki 2 kolom
        assert result == [[1.0,2.0],[3.0,4.0]]

    def test_reshape_matrix_missmatch(self) -> None: 
        """Memastikan ValueError dilempar jika perkalian dimensi tidak cocok dengan total elemen."""
        raw_data = [1,2,3]
        dimensions = (2,2)
        # Robot uji harus menangkap ValueError
        with pytest.raises(ValueError) as exc_info:
            self.transformer.reshape_matrix(raw_data, dimensions)
        # Memastikan potongan kata pesan error sesuai
        assert "Kesalahan Dimensi!" in str(exc_info.value)
    
