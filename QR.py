import qrcode
import os

# Version - size --- 1 to 40
pj = qrcode.QRCode(version=20, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=5, border=4)  # box size use to manage small boxes inside QRCODE
pj.add_data("https://www.linkedin.com/in/prince-kumar-jha-037568285/")
pj.make(fit=True)

img = pj.make_image(fill_color="black", back_color="white")  # make helps to create image and save in location

# Define the path to save the QR code image
save_path = "C:/Users/jhap9/OneDrive/Desktop/dev vscode/Projects/QR Generator/QR.png"

# Ensure the directory exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the image
img.save(save_path)