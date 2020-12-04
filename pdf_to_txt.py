from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os

# create directory for clean articles if doesn't exist yet
save_path = 'ereview_good_txt'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# get all pdf files
file_path = 'ereview_pdf'
files = os.listdir(file_path)
total_files = len(files)

# got thru all pdf files
for i, file in enumerate(files):
    if os.path.exists(save_path + '/' + file[0:-4] + '.txt'):
        print('Converted file ', i + 1, ' out of ', total_files)
        continue
    else:
        # get pdf pages
        file_name = file_path + '/' + file
        pages = convert_from_path(file_name, 500)

        # convert pages to JPEG and save
        count = 0
        for page in pages:
            count += 1

            filename = 'page_' + str(count) + '.jpg'

            page.save(filename, 'JPEG')

        # open text file w same file name
        text_file = file[0:-4] + '.txt'
        f = open(save_path + '/' + text_file, 'a')

        # convert JPEGs to text file
        for num in range(1, count + 1):

            # get JPEG file for page
            page_name = "page_" + str(num) + ".jpg"

            # convert to text string
            text = str((pytesseract.image_to_string(Image.open(page_name))))
            text = text.replace('-\n', '')

            # store good text in new file
            f.write(text)

            # delete JPEG file from main dir
            os.remove(page_name)

        f.close()
        print('Converted file ', i + 1, ' out of ', total_files)