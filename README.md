# Motion Analysis and Posture Monitoring System Using Biomedical Sensors

## Project Overview

This project provides a wearable biomedical system to monitor and improve posture and mobility. Sensors positioned at key anatomical points collect real-time data, which is processed using Python-based algorithms and FPGA technology to give immediate feedback, assisting users in maintaining proper posture and preventing musculoskeletal issues.

## Table of Contents
- [Project Overview](#project-overview)
- [Motivation](#motivation)
- [Software Architecture](#software-architecture)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [License](#license)

## Motivation

With modern lifestyles leading to common postural problems, this system addresses the need for real-time posture monitoring. Using an FPGA for rapid data processing and Python for algorithmic analysis, this project offers immediate corrective feedback and insights into postural health.

## Software Architecture

The system’s modular design separates data acquisition, processing, and feedback:

1. **Data Acquisition Layer (Biomedical Sensors):**
   - Sensors collect angles and deviations from key body areas and send data wirelessly for real-time analysis.

2. **Data Processing Layer (FPGA):**
   - An FPGA preprocesses the sensor data for efficient pipeline delivery to Python-based analysis.

3. **Analysis and Feedback Layer (Python):**
   - Algorithms detect posture deviations, alert users, and log data for progress tracking.
   
4. **User Interface Layer:**
   - A dashboard visualizes real-time metrics, historical trends, and feedback for a seamless user experience.

## Features
- **Real-Time Posture Feedback:** Instant correction guidance.
- **Wearable Sensors:** Comfortable, everyday use.
- **FPGA Processing:** Optimized low-latency response.
- **Python-Based Analysis:** Detection of posture deviations using machine learning.
- **User-Friendly Dashboard:** Real-time visualization and trend analysis.

## Requirements
- **Hardware:**
  - Biomedical sensors
  - FPGA
- **Software:**
  - Python (>=3.8)
  - Libraries: scikit-learn, TensorFlow, SciPy, etc.
  - FPGA programming tools

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SteveProkovas/Motion-Analysis-and-Posture-Monitoring-System.git
   cd Motion-Analysis-and-Posture-Monitoring
   ```
2. Install Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up and configure the FPGA.

## Usage
1. Connect sensors to the specified body points.
2. Run the data acquisition program:
   ```bash
   python acquisition.py
   ```
3. Start the main application for real-time feedback:
   ```bash
   python main.py
   ```

## Code Overview

Here’s a brief look at some main functions of the project:

### **Main Application**: `PostureMonitorApp`

```python
class PostureMonitorApp(tk.Tk):
    def __init__(self):
        # Initialize model and logger
        self.model = PostureDetectionModel()
        self.logger = DataLogger()
        ...
        
    def acquire_sensor_data(self):
        """Simulates acquiring data from sensors."""
        return {
            'hip_flexion': random.uniform(-45, 45),
            'knee_extension': random.uniform(0, 90),
            'spine_angle': random.uniform(-30, 30)
        }

    def update_monitoring(self):
        """Real-time posture feedback."""
        while self.monitoring:
            sensor_data = self.acquire_sensor_data()
            self.update_ui(sensor_data)
            issues = self.model.predict(sensor_data)
            self.logger.log(sensor_data, issues)
            ...
```

### **Posture Prediction Model**: `PostureDetectionModel`

```python
class PostureDetectionModel:
    def __init__(self):
        self.model = LogisticRegression()  # Placeholder for an actual ML model
        
    def predict(self, sensor_data):
        """Predicts posture issues based on thresholds or ML classifications."""
        predictions = []
        if sensor_data['hip_flexion'] > 30 or sensor_data['hip_flexion'] < -30:
            predictions.append("Hip Flexion Issue")
        if sensor_data['knee_extension'] < 15:
            predictions.append("Knee Extension Issue")
        if sensor_data['spine_angle'] > 20 or sensor_data['spine_angle'] < -20:
            predictions.append("Spine Angle Deviation")
        return predictions
```

### **Data Logging**: `DataLogger`

```python
class DataLogger:
    def __init__(self, filename="posture_log.csv"):
        self.filename = filename
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Hip Flexion", "Knee Extension", "Spine Angle", "Issues"])
    
    def log(self, sensor_data, issues):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now(),
                sensor_data['hip_flexion'],
                sensor_data['knee_extension'],
                sensor_data['spine_angle'],
                "; ".join(issues)
            ])
```

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
