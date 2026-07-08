# debug_path.py
import os
from src.signal_processor import SignalProcessor

# 1. Cetak lokasi fisik file yang diimpor oleh Python
print("\n" + "="*60)
print("LOKASI FILE YANG DIBACA OLEH PYTHON:")
print(os.path.abspath(SignalProcessor.__module__))
print("="*60)

# 2. Cetak fungsi apa saja yang ada di dalam Class tersebut
print("\nDAFTAR FUNGSI YANG TERDETEKSI:")
print(dir(SignalProcessor))
print("="*60 + "\n")