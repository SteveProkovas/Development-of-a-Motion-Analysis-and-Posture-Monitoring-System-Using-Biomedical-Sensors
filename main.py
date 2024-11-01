import tkinter as tk
from tkinter import ttk
import random
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from sklearn.linear_model import LogisticRegression  # Placeholder for an actual ML model
from datetime import datetime
import csv
from pygrabber.dshow_graph import FilterGraph


# Simulated Machine Learning Model for Posture Detection
class PostureDetectionModel:
    def __init__(self):
        self.model = LogisticRegression()

    def predict(self, sensor_data):
        predictions = []
        if sensor_data['hip_flexion'] > 30 or sensor_data['hip_flexion'] < -30:
            predictions.append("Hip Flexion Issue")
        if sensor_data['knee_extension'] < 15:
            predictions.append("Knee Extension Issue")
        if sensor_data['spine_angle'] > 20 or sensor_data['spine_angle'] < -20:
            predictions.append("Spine Angle Deviation")
        return predictions


# Data Logger
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


# Main Application
class PostureMonitorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Real-Time Posture Monitor")
        self.geometry("800x600")

        # Initialize Model and Logger
        self.model = PostureDetectionModel()
        self.logger = DataLogger()

        # Initialize camera ID to None
        self.camera_id = None
        self.monitoring = False

        # UI Elements
        self.create_ui()

    def create_ui(self):
        self.label = tk.Label(self, text="Real-Time Posture Feedback", font=("Arial", 16))
        self.label.pack(pady=10)

        self.camera_selector_label = tk.Label(self, text="Select Camera:", font=("Arial", 12))
        self.camera_selector_label.pack(pady=5)

        self.camera_selector = ttk.Combobox(self, state="readonly")
        self.camera_selector["values"] = self.detect_cameras()
        self.camera_selector.pack(pady=5)

        self.output_frame = tk.Frame(self)
        self.output_frame.pack(pady=20)

        self.hip_label = tk.Label(self.output_frame, text="Hip Flexion: 0°", font=("Arial", 12))
        self.hip_label.grid(row=0, column=0, padx=10)

        self.knee_label = tk.Label(self.output_frame, text="Knee Extension: 0°", font=("Arial", 12))
        self.knee_label.grid(row=1, column=0, padx=10)

        self.spine_label = tk.Label(self.output_frame, text="Spine Angle: 0°", font=("Arial", 12))
        self.spine_label.grid(row=2, column=0, padx=10)

        self.alert_label = tk.Label(self, text="", font=("Arial", 12), fg="red")
        self.alert_label.pack(pady=10)

        self.start_button = ttk.Button(self, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.pack(pady=10)

        # Matplotlib Figure for Real-Time Plot
        self.fig, self.ax = plt.subplots(3, 1, figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack()

        # For live data plotting
        self.data_history = {"hip_flexion": [], "knee_extension": [], "spine_angle": []}

    def detect_cameras(self):
        """Uses pygrabber to detect connected cameras."""
        graph = FilterGraph()
        devices = graph.get_input_devices()
        return devices

    def start_monitoring(self):
        """Starts the posture monitoring in a separate thread."""
        selected_camera = self.camera_selector.get()
        if not selected_camera:
            self.alert_label.config(text="Please select a camera.")
            return

        self.camera_id = self.camera_selector.current()
        if not self.monitoring:
            self.monitoring = True
            threading.Thread(target=self.update_monitoring, daemon=True).start()

    def acquire_sensor_data(self):
        """Simulates acquiring data from sensors placed on key body points."""
        return {
            'hip_flexion': random.uniform(-45, 45),
            'knee_extension': random.uniform(0, 90),
            'spine_angle': random.uniform(-30, 30)
        }

    def update_monitoring(self):
        """Updates the posture data and feedback in real time."""
        while self.monitoring:
            sensor_data = self.acquire_sensor_data()
            self.update_ui(sensor_data)
            issues = self.model.predict(sensor_data)
            self.logger.log(sensor_data, issues)

            if issues:
                self.alert_label.config(text="Posture Alerts: " + "; ".join(issues))
            else:
                self.alert_label.config(text="Posture is normal.")
            self.update_plot(sensor_data)
            time.sleep(1)

    def update_ui(self, sensor_data):
        """Updates the text labels in the UI with current sensor data."""
        self.hip_label.config(text=f"Hip Flexion: {sensor_data['hip_flexion']:.2f}°")
        self.knee_label.config(text=f"Knee Extension: {sensor_data['knee_extension']:.2f}°")
        self.spine_label.config(text=f"Spine Angle: {sensor_data['spine_angle']:.2f}°")

    def update_plot(self, sensor_data):
        """Updates the real-time data plot."""
        for key, value in sensor_data.items():
            self.data_history[key].append(value)
            if len(self.data_history[key]) > 50:
                self.data_history[key].pop(0)

        self.ax[0].cla()
        self.ax[0].plot(self.data_history["hip_flexion"], color="blue")
        self.ax[0].set_title("Hip Flexion")

        self.ax[1].cla()
        self.ax[1].plot(self.data_history["knee_extension"], color="green")
        self.ax[1].set_title("Knee Extension")

        self.ax[2].cla()
        self.ax[2].plot(self.data_history["spine_angle"], color="red")
        self.ax[2].set_title("Spine Angle")

        self.canvas.draw()

    def stop_monitoring(self):
        """Stops the posture monitoring."""
        self.monitoring = False
        self.alert_label.config(text="Monitoring stopped.")


if __name__ == "__main__":
    app = PostureMonitorApp()
    app.protocol("WM_DELETE_WINDOW", app.stop_monitoring)
    app.mainloop()
