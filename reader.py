from PIL import Image
import pytesseract 
import os
import sys
import readline
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")

def fileName():
	file_name = "aysha.jpg".strip()
	if not file_name:
		file_name = 'imageText'
	return file_name	
def imagePath():	
	image_path ="text.txt"
	if os.path.exists(image_path):
		image_path = image_path
	else:
		print(f"The file F:\Basem\kjh does not exist")
		imagePath()
	return image_path

if __name__ == '__main__':
	try:
		file_name = fileName()

		image = imagePath()
		while os.path.exists(image) != True:
			image = imagePath()

		with open(file_name,"w") as f:
			itx = pytesseract.image_to_string(image,lang='eng')
			f.write(itx)
	except KeyboardInterrupt:
		print("---interrupted---")
		sys.exit()
	except Exception as e:
		print("try again")
		sys.exit()