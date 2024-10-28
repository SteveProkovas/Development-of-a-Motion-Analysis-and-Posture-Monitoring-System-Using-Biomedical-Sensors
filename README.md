# Development of a Motion Analysis and Posture Monitoring System Using Biomedical Sensors

## Project Overview

This project focuses on creating a wearable biomedical system for monitoring and improving body posture and mobility. Utilizing sensors strategically placed on key body areas (e.g., back, neck, knees), the system records data on movement and posture in real time. This data is analyzed using Python algorithms incorporating discrete mathematics and machine learning, providing immediate feedback to users. A Field-Programmable Gate Array (FPGA) serves as the backbone for digital control and processing, enabling rapid, real-time feedback.

## Table of Contents
- [Project Overview](#project-overview)
- [Motivation](#motivation)
- [Software Architecture](#software-architecture)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Motivation

Modern lifestyles often lead to poor posture and increased risk of musculoskeletal issues, impacting both physical health and quality of life. Existing posture-monitoring systems are often limited by either processing speed, delayed feedback, or lack of real-time analysis. This project aims to address these limitations by integrating robust data processing capabilities with a wearable, real-time system. By leveraging FPGA technology alongside Python-based data analysis, this solution aims to ensure timely, accurate feedback and improve user mobility and posture through prompt corrective action.

## Software Architecture

The system’s software architecture is modular, enabling clear separation of functionalities for efficient data acquisition, processing, and feedback delivery.

1. **Data Acquisition Layer (Biomedical Sensors):**
   - Sensors, including accelerometers and gyroscopes, are strategically placed at key anatomical points.
   - Sensor data is collected on angular movements, rotations, and orientations, generating metrics such as joint angles and posture deviations.
   - A low-power, wireless protocol is used for data transmission to reduce latency and optimize power usage.

2. **Data Processing Layer (FPGA):**
   - Sensor data streams into an FPGA, which performs initial filtering, aggregation, and normalization of raw data.
   - The FPGA handles real-time data synchronization from various sensor nodes and sends pre-processed data to the main analysis unit.
   - Rapid, hardware-level data management ensures minimal delays in user feedback.

3. **Analysis and Feedback Layer (Python and Discrete Mathematics):**
   - The processed data is analyzed by algorithms written in Python that utilize discrete mathematics and machine learning.
   - Algorithms detect abnormal posture or deviations based on established patterns and standards.
   - If an issue is detected, the system issues alerts or corrective feedback to the user via a mobile or desktop interface.
   - Data is logged for historical tracking and further analysis to aid in personalized posture correction strategies.

4. **User Interface Layer:**
   - A user-friendly dashboard displays real-time posture information, historical data trends, and corrective action suggestions.
   - The interface integrates notifications for posture correction and supports customizable settings for alerts and feedback.

## Features
- **Real-Time Posture Detection and Monitoring:** Continuous tracking of posture with immediate feedback for correction.
- **Wearable Sensor System:** Compact, low-profile sensors that maintain user comfort and minimize restrictions on mobility.
- **Data Processing with FPGA:** High-speed data handling and processing to ensure low-latency feedback.
- **Python-Based Algorithmic Analysis:** Machine learning and discrete mathematics algorithms detect posture deviations.
- **User-Friendly Interface:** Intuitive UI for real-time visualization and historical trend analysis.

## Requirements
- **Hardware:**
  - Biomedical sensors (accelerometers, gyroscopes)
  - FPGA for data processing
  - Computer or mobile device for data display
- **Software:**
  - Python (>=3.8)
  - Machine learning libraries (e.g., scikit-learn, TensorFlow)
  - Discrete mathematics libraries (e.g., SciPy)
  - FPGA programming tools (specific to chosen hardware)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SteveProkovas/Motion-Analysis-and-Posture-Monitoring.git
   cd Motion-Analysis-and-Posture-Monitoring
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Follow the FPGA setup documentation to configure and deploy the FPGA program.

## Usage
1. Connect the sensors to the target body points as specified.
2. Run the data acquisition program.
   ```bash
   python acquisition.py
   ```
3. Visualize and monitor posture in real-time through the provided user interface:
   ```bash
   python main.py
   ```

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
