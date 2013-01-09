import base64
from robofab.interface.all.dialogs import GetFile


# or give full path
f = GetFile()

# use mode = "rb" to read binary file
fin = open(f, "rb")
binary_data = fin.read()
fin.close()

# encode binary to base64 string (printable)
b64_data = base64.b64encode(binary_data)

print b64_data
