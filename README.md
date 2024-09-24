<div align="center">

# 📟 UniTrack Scanner

Hardware unit code for capturing student attendance data using RFID technology.

</div>

## 📝 Introduction

Easily track student attendance with the UniTrack Scanner. Designed for use in physical university campuses, this tool communicates with our dashboard for seamless data integration, helping automate attendance monitoring using RFID readers and GPIO pins on Raspberry Pi hardware.

## 🚀 Features

- 🎓 **Attendance Capture**: Efficiently scan student RFID cards to record attendance.
- 🔗 **Seamless Dashboard Integration**: Automatically syncs captured data with the UniTrack Dashboard for real-time analytics.
- 📡 **Hardware Integration**: Leverages Raspberry Pi and RFID technology for accurate attendance tracking.
- 💡 **Customizable GPIO Pins**: Configure GPIO pins for additional functionality (RGB, readers).

## 🛠️ Tech Stack

- **Python 3.11** - Main programming language for the hardware control.
- **Raspberry Pi** - Hardware unit used for RFID scanning and GPIO control.
- **MFRC522** - Python library for interacting with RFID readers.
- **PyGPIO** - GPIO control library for interacting with Raspberry Pi pins.

## 🚀 Getting Started

### Prerequisites

- Python 3.11 installed
- Raspberry Pi with GPIO and RFID hardware
- Internet connection for syncing attendance data

### Installation

1. Clone the repository:

```bash
git clone https://github.com/UniTrackApp/scanner.git
cd scanner
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up the Raspberry Pi environment and ensure GPIO pins are configured correctly. Refer to the following guides:

- [MFRC522 Documentation](https://pypi.org/project/mfrc522-python/)
- [Raspberry Pi GPIO Pin Setup](https://packaging.python.org/en/latest/tutorials/installing-packages/)

4. Start the scanner:

```bash
python src/scanner.py
```

## ✌️ Team

- [Aryan Prince](https://x.com/aryxnprince)
- [Andrea La Fauci De Leo](https://github.com/Bosurgi)
- [Lewis Johnson](https://github.com/lewisj576)

## 🔑 License

- [GNU GPLv3](https://github.com/UniTrackApp/dashboard/blob/main/COPYING).
