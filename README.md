
# PetPredictor: Website for Cat and Dog Classification

Project Description:

The "PetPredictor" Website is an interactive online tool designed to predict whether an uploaded image contains a dog or a cat. Users can upload images of their pets or other animals, and the website's machine learning model will quickly analyze the image and provide a prediction. The website aims to offer a fun and engaging way for users to determine whether an image features a canine or a feline subject.

Intended Audience:

The "PetPredictor" Website is intended for animal lovers, pet owners, and anyone curious about machine learning-based image classification. It's user-friendly and accessible, making it suitable for people of all ages who enjoy interacting with technology. Whether users want to showcase their adorable pets, test the model's accuracy, or simply have some fun, the website provides an easy and entertaining way to engage with image recognition technology.








## Deployment

1.download zip file and extratct wherever you want.

2.open the command prompt and download dependency by using below given command.
```bash
  pip install Flask tensorflow pillow

```
3. navigating to the dog_cat_classifier directory, and running the following command:
```bash
python app.py
```
4. Once you run the command, you'll see the output indicating that the Flask development server is running. Open your web browser and go to http://127.0.0.1:5000/. You'll see your web application's interface where you can upload an image.
## file structure
dog_cat_classifier/

│   app.py

└───pretrained_model/

│       pretrained_mdel.keras

│
└───templates/

│       index.html




