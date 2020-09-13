####以下为使用模型进行训练的代码!
####load model的代码只能加载一次，放在init中，否则会报错

from keras.models import load_model
import os
import numpy as np
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input

model=None

def read_image(img_name):
    print('imagename:'+img_name)
    img = image.load_img(img_name, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x

def predict(imagepath):
    categories=['bad','good','green','normal','red']
    global model
    if model != None:
        img=read_image(imagepath)
        print('readimage successful')
        prediction=model.predict(img)
        result=categories[int(prediction[0][0])]
        print(result)
        return result
    else:
        print('predict else')
        return "error"

if os.path.exists('app//inception_1.h5'):
    print('predict if')
    model = load_model('app//inception_1.h5',compile=False)
    print('load successful')
    print(model.predict(read_image('app//necessary.PNG')))


