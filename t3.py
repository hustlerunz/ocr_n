import datetime
import io
import pdf2image
import pytesseract
from PIL import Image
from flask import Flask, request, render_template, redirect, url_for, session
from pdf2image import convert_from_path ,convert_from_bytes

app = Flask(__name__)

# Secret key for sessions encryption
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)

def ocr_core(file):
    text = pytesseract.image_to_string(file,lang='tha+eng')
    return text

def print_pages(pdf_file):
    images = pdf_to_img(pdf_file)
    for pg, img in enumerate(images):
        print(ocr_core(img))

@app.route('/')
def home():
    return render_template("index.html", title="Image Reader")

@app.route('/scanner', methods=['GET', 'POST'])
def scan_file():
    sum_result =""
    global s2_data
    s2_data = [] 
    if request.method == 'POST':
        start_time = datetime.datetime.now()
        image_data = request.files['file'].read()
        name = request.files['file'].filename
        print("name = "+name)
        check_name = ".pdf" in name
        if check_name == True:
            print("file_pdf = true")
            #dpd2images = convert_from_path(io.BytesIO(image_data))
            dpd2images = convert_from_bytes(image_data)
            print(dpd2images)
            for pg, img in enumerate(dpd2images):
                print(ocr_core(img))
                sum_result += ocr_core(img)
            s2_data = [{
                    "text": sum_result,
                    "time": str((datetime.datetime.now() - start_time).total_seconds())
                }]  
            return redirect(url_for('result'))
        else:    
            scanned_text = pytesseract.image_to_string(Image.open(io.BytesIO(image_data)),lang='tha+eng')
            print("Found data:", scanned_text)
            s2_data = [{
                        "text": scanned_text,
                        "time": str((datetime.datetime.now() - start_time).total_seconds())
                    }]
            return redirect(url_for('result'))
    
@app.route('/result')
def result():
        
    if "s2_data" in globals():
        data = s2_data
        print("data = ",s2_data[0]['time'])
        return render_template(
            "result.html",
            title="Result",
            time="1234",
            text=data[0]["text"],
            words=len(data[0]["text"].split(" "))
    )
    else:
        return "Wrong request method."

if __name__ == '__main__':
    # Setup Tesseract executable path
    #pytesseract.pytesseract.tesseract_cmd = r'D:\TesseractOCR\tesseract'
    pytesseract.pytesseract.tesseract_cmd = r'tesseract'
    app.run(host='0.0.0.0', port=5001,debug=True)