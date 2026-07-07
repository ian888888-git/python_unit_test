import pytest 
from metrics import MetricsCalculator

class TestMetricsCalculator: 
    """Class Unit Testing untuk memastikan validitas logika di MetricsCalculator."""

    @pytest.fixture(autouse=True)
    def setup(self)->None:
        """Skenario awal untuk instansiasi objek sebelum setiap fungsi test berjalan."""
        self.calculator = MetricsCalculator()

    def test_evaluate_record_success_above_treshold(self) -> None:
        """Memastikan data dengan akurasi >= 95.0% dinyatakan lolos (True)."""
        # Eksekusi fungsi dengan 3 parameter
        msg, score, status = self.calculator.evaluates_record(100, 96, "testing_unit")

        # Assertions
        assert msg == "SUKSES"
        assert score == 96.0
        assert status == True 
        assert isinstance((msg, score, status), tuple) # Memastikan tipe kembalian murni Tuple
    
    def test_evaluate_record_fail_below_treshold(self) -> None:
        """Memastikan data dengan akurasi < 95.0% dinyatakan butuh revisi (False)."""
        msg, score, status =  self.calculator.evaluates_record(100, 93, "testing_unit")

        assert "BUTUH_REVISI" in msg 
        assert score == 93.0 
        assert status == False 
        # assert isinstance((msg, score, status), tuple)
    
    def test_evaluate_record_fail_zero(self) -> None:
        """Memastikan sistem tidak crash (ZeroDivisionError) jika total data bernilai 0."""
        msg, score, status =  self.calculator.evaluates_record(0, 0, "testing_unit")

        assert "GAGAL" in msg 
        assert score == 0.0 
        assert status == False 




