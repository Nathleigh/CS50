# Harvard CS50P week 8 OOP
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 50)
pdf.cell(0, 30, "CS50 Shirtificate", align="C")
# Add background image
pdf.image("shirtificate.png", x=10, y=50, w=190)
username = input("Name: ")
# Add text over the background
pdf.set_font("helvetica", "B", 30)
pdf.set_text_color(255, 255, 255)  # Set text color to white
pdf.set_xy(10, 110)  # Set position for the text
pdf.cell(0, 10, username, ln=True, align="C")
pdf.output("shirtificate.pdf")
