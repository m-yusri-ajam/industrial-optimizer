import pandas as pd
import numpy as np

def generate_process():
    readings = 500
    temp = np.random.normal(180, 10, readings)
    # Purity formula: Max at 180°C, drops as you move away
    purity = 91 - (abs(temp - 180) * 0.4) + np.random.normal(0, 0.5, readings)
    
    df = pd.DataFrame({'Temp_C': temp, 'Purity_%': purity})
    df.to_csv('data/process_telemetry.csv', index=False)
    print("✅ Industrial Seed Data Created.")

if __name__ == "__main__":
    generate_process()
