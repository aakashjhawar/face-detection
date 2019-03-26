# import libraries
import cv2
import sys
import numpy as np

def load_model(image_path):
    # load serialized model from disk
    net = cv2.dnn.readNetFromCaffe('deploy.prototxt.txt','res10_300x300_ssd_iter_140000.caffemodel')
    
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
    	(300, 300), (104.0, 177.0, 123.0))

    # pass the blob through the network and obtain the detections and
    # predictions
    net.setInput(blob)
    detections = net.forward()

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the
        # prediction
        confidence = detections[0, 0, i, 2]
        
        # filter out weak detections by ensuring the `confidence` is greater than the minimum confidence
        '''you can also change the 'confidence' (0.5 here) for better results'''
        if confidence > 0.5:
            # compute the (x, y) coordinates of the bounding box for the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            #print('detections', detections[0, 0, i, 3:7])
            #print('box', box)
            # draw the bounding box of the face along with the associated probability
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
            cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
    
    # Show the output image
    while True:
        cv2.imshow("Output", image)
        # Close windows with Esc
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    
    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    #image_path = 'aakash1.jpg'
    #load_model(image_path)
    try:
        load_model(image_path = sys.argv[1])
    except:             #    except IndexError:
        fmt = 'usage: {} image_path'
        print(fmt.format(__file__.split('/')[-1]))
        print('[ERROR]: Image not found')