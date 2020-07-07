import os, sys
from app import app
from flask import jsonify, request
from PIL import Image

# routes - /image/convert/ - route to convert images
@app.route('/image/convert', methods=['POST', 'GET'])
def image():

    response = {'res':'', 'err':''}

    if request.method == 'POST':

        # input data
        convert_type = str(request.form['convert_type']).upper()
        input_img = request.files['input_img']

        # convert process
        img = Image.open(input_img)
        converted_img = ''
        
        # it only converts different data types
        if img.format == 'JPEG' and convert_type != 'JPEG':
            
            # converts to JPEG 
            converted_img = img.convert('RGB')
            converted_img.save('converted_image.jpg', convert_type)  # the image can be found in the root dir of virutalenv
            converted_img.format = convert_type
            
            img_info = {'format': converted_img.format,'size':converted_img.size,'mode':converted_img.mode, 'PIL_obj': str(converted_img)}

            response['res'] = img_info

        # it only converts different data types
        elif img.format == 'PNG' and convert_type != 'PNG':
            
            # converts to PNG        
            converted_img = img.convert('RGB')
            converted_img.save('converted_image.png', convert_type) # the image can be found in the root dir of virutalenv
            converted_img.format = convert_type

            img_info = {'format': converted_img.format,'size':converted_img.size,'mode':converted_img.mode, 'PIL_obj': str(converted_img)}

            response['res'] = img_info
        else:
            response['err'] = 'INCORRECT TYPE OF INPUT FILE'

        return response

    else:
        response['err'] = 'INVALID METHOD!'
    
    return response