#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Generating SOC logs..."
python soc_attack_simulation/attack_simulator.py

echo "Starting SOC dashboard..."
streamlit run soc_dashboard/dashboard.py
