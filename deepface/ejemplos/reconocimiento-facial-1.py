from deepface import DeepFace
obj = DeepFace.analyze(img_path = "/home/daniel/Documentos/GitHub/apertura-puertas-reconocimiento-facial/deepface/faces/image1.jpeg", 
        actions = ['age', 'gender', 'race', 'emotion']
)
print("analisis de la imagen1")
print(obj)