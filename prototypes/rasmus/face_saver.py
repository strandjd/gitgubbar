import cv2, os

def save_faces(pathin, dirout):

    if not os.path.isfile(pathin) or not os.path.isdir(dirout):
        return -1

    img = cv2.imread(pathin)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for i, (x, y, w, h) in enumerate(faces):
        face = img[y:y + h, x:x + w]
        pathout = f'{dirout}/{i}.jpg'
        cnt = i
        while os.path.isfile(pathout):
            cnt += 1
            pathout = f'{dirout}/{cnt}.jpg'
        cv2.imwrite(pathout, face)

    return len(faces)

def transform_faces(dirin, dirout):
    pass

if __name__=='__main__':
    import glob

    if not os.path.isdir('res'):
        os.mkdir('res')
    
    for f in glob.glob('res/*'):
        os.remove(f)

    print(save_faces('human.jpg', 'res'))
