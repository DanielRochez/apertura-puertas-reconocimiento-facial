from deepface import DeepFace
print("Cargando imagenes para su comparación...")
result = DeepFace.verify(img1_path = "/home/daniel/Documentos/GitHub/apertura-puertas-reconocimiento-facial/deepface/faces/image1.jpeg", img2_path = "/home/daniel/Documentos/GitHub/apertura-puertas-reconocimiento-facial/deepface/faces/image3.jpeg")
print("Resultados")
print(result)