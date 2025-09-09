# Smart-Waste-Segregation-System
The Smart Waste Segregation System is an automated solution designed to classify household and municipal waste into metal, wet, and dry categories using Arduino, sensors, and servo motors. The system reduces human effort, enhances efficiency, and promotes a cleaner environment by sorting waste at the source.
# Smart Waste Segregation System ♻️
An Arduino + Python based project that automatically classifies waste into Metal, Wet, and Dry categories using sensors and servo motors.

- [About](#about)  
- [Features](#features)  
- [Hardware Requirements](#hardware-requirements)  
- [Software Requirements](#software-requirements)  
- [Circuit Diagram](#circuit-diagram)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Workflow](#project-workflow)  
- [Future Scope](#future-scope)  
- [Authors](#authors)  

## About  
The Smart Waste Segregation System is an automated solution to sort waste into **Metal, Wet, and Dry** categories.  
It uses an **IR sensor, Moisture sensor, and Metal detector** along with an **Arduino UNO and Servo motor** to reduce human effort and promote sustainable recycling.  

🔌 Hardware Components

Arduino UNO R3

Microcontroller board (ATmega328P)
Controls the entire system

IR Sensor (Infrared Obstacle Detection Sensor)
Detects the presence of waste at the input chute

Metal Detector Sensor
Identifies metallic waste (ferrous/non-ferrous objects)

Moisture Sensor (Soil Hygrometer Sensor)
Measures moisture to distinguish wet waste from dry waste

Servo Motor (SG90 / MG90S)
Rotates to direct waste into the correct bin (0°, 90°, 180°)

Jumper Wires (Male-Male, Male-Female, Female-Female)
For making connections between Arduino, sensors, and servo

Breadboard (optional, for prototyping)
To connect sensors and organize wiring

Power Supply
Arduino powered via USB (5V)
Optional external 5V supply for servo (if multiple motors are used)

Waste Bins / Containers
Three bins: Metal Bin, Wet Bin, Dry Bin

USB Cable (Type A to B)
To connect Arduino UNO to PC (for coding + power)

## Features  
- Automatically detects and sorts waste using sensors.  
- Classifies waste into **Metal, Wet, and Dry** categories.  
- Servo motor directs waste into correct bins.  
- Python integration for data processing and logging.  
- Low-cost, scalable, and easy to build.  

## Hardware Requirements  
- Arduino UNO  
- IR Sensor  
- Moisture Sensor  
- Metal Detector Sensor  
- Servo Motor  
- Jumper wires, Breadboard, Power supply  

## Software Requirements  
- Arduino IDE  
- Python 3.x  
- Libraries: [pyserial](https://pypi.org/project/pyserial/)  



## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/smart-waste-system.git
   cd smart-waste-system

pip install pyserial


---

### 9. **Usage**
```markdown
## Usage  
1. Connect Arduino to your computer via USB.  
2. Run the Python script:  
   ```bash
   python waste_sorter.py


---
Place waste in front of sensors.

Metal → Servo moves to 0°

Wet → Servo moves to 90°

Dry → Servo moves to 180°
### 10. **Project Workflow**
(Optional: Add a flowchart from your research paper showing how detection works.)  

---

### 11. **Future Scope**
```markdown
## Future Scope  
- IoT integration for real-time waste monitoring.  
- Cloud dashboard for waste analytics.  
- AI-based image recognition for more accurate classification.  

