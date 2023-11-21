import bson
from bson.binary import Binary

with open("/Users/anshin-lin/Downloads/Anhsin-removebg-preview.png", "rb") as f:
    encoded = Binary(f.read()) 
    print(encoded)
    print(type(encoded) == Binary)