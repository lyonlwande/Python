#12. Display Products with Numbers
"""
Create a list of products and display them like:

1. Laptop
2. Mouse
3. Keyboard
"""
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Headphones", "Webcam", "Speaker", "Microphone", "External Hard Drive"]

for x in range(len(products)) :
    print(f"{x+1}.{products[x]}")
