from flask import Flask, render_template, request
import imageProcessing
import captureTemplate
import twoPics

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./home.html')

@app.route('/select')
def select():
    return render_template('./select.html')

@app.route('/weight')
def weight():
    return render_template('./weight.html')

@app.route('/end')
def end():
    return render_template('./end.html')

@app.route('/fire')
def fire():
    return render_template('./fire.html')

@app.route('/capture')
def capture():
    return render_template('./image_capture.html')

@app.route('/strap')
def strap():
    return render_template('./strap.html')

@app.route('/simpleAnalysis', methods=['POST', 'GET'])
def simpleAnalysis():
    # Get data from the request
    base64image = request.form['base64image']
    imagePath = request.form['imagePath']
    
    # Save unprocessed image to the database
    imageProcessing.base64_to_image(base64image, imagePath)
    
    # Process the data (dummy function for demonstration)
    processed_data = imageProcessing.process_and_save_image(imagePath, 0)
    
    # Return the processed data as a response
    return processed_data

@app.route('/mlAnalysis', methods=['POST', 'GET'])
def mlAnalysis():
    # Get data from the request
    base64image = request.form['base64image']
    imagePath = request.form['imagePath']
    
    # Save unprocessed image to the database
    imageProcessing.base64_to_image(base64image, imagePath)
    
    # Process the data (dummy function for demonstration)
    processed_data = imageProcessing.main(imagePath)
    
    # Return the processed data as a response
    return processed_data

@app.route('/captureTemplate', methods=['POST', 'GET'])
def capTemplate():
    captureTemplate.main()
    return "0"

@app.route('/liveAnalysis', methods=['POST', 'GET'])
def liveAnalysis():
    twoPics.main()
    return "0"

if __name__ == '__main__':
    app.run()
