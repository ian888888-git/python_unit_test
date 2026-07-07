# Automated Data Pipeline & MLOps Quality Gate

Proyek ini adalah blueprint *Automated Data Pipeline* berbasis Python yang dirancang menggunakan pendekatan **Modular Object-Oriented Programming (OOP)**. Sistem ini dilengkapi dengan gerbang kualitas data otomatis (*Quality Gate*) melalui pipeline **Continuous Integration (CI)** menggunakan GitHub Actions.

## 📌 Arsitektur Proyek

Proyek ini memisahkan secara tegas antara logika bisnis aplikasi (di dalam folder `src/`), skrip pengujian (di dalam folder `tests/`), dan konfigurasi infrastruktur DevOps di root folder.

```text
py-unit-test-project/
│
├── .github/
│   └── workflows/
│       └── ci-pipeline.yml   # Konfigurasi Pipa Automation CI (GitHub Actions)
│
├── src/                      # Source Code Utama Aplikasi
│   ├── __init__.py
│   ├── cleaner.py            # Modul Pembersihan Data Teks & Sensor (OOP)
│   ├── metrics.py            # Modul Kalkulator Metrik Kualitas (Multi-Parameter)
│   ├── pipeline.py           # Orchestrator / Pengatur Aliran Data Pipeline
│   └── main.py               # Entry Point / Pelatuk Ringan Aplikasi
│
├── tests/                    # Folder Khusus Unit Testing
│   ├── __init__.py
│   └── test_metrics.py       # File Pengujian Otomatis via Pytest
│
└── requirements.txt          # Daftar Pustaka Pihak Ketiga (Dependencies)