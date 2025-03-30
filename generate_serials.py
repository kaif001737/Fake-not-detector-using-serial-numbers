import pandas as pd
import random

# Function to generate random serial numbers
def generate_serial_numbers(count=100000):
    serials = []
    
    # List of 2-letter prefixes (RBI printing press codes for dataset)
    prefixes = ['AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ',
                'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ',
                'KA', 'KB', 'KC', 'KD', 'KE', 'KF', 'KG', 'KH', 'KI', 'KJ']
    
    for _ in range(count):
        prefix = random.choice(prefixes)  # Random 2-letter prefix
        number = str(random.randint(100000, 999999))  # Random 6-digit number
        serials.append(prefix + number)  # Combine to form serial number
    
    return serials

# Generate dataset
serial_numbers = generate_serial_numbers()

# Save to CSV file
df = pd.DataFrame(serial_numbers, columns=["Serial Number"])
df.to_csv("serial_numbers.csv", index=False)

print("✅ 100,000 real-looking serial numbers saved to 'serial_numbers.csv'.")
