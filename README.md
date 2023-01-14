# RagaIdent
Music plays a key role in the life of every living being. The last two decades has seen an exponential growth in the number and variety of songs created.
In accordance to classical music notes and ragas are the lifeline of any song. For an artist to be able to do full justice to a song, the notes and ragas for every composition play a key role.
Not all artists are gifted note and raga identifiers. Any artist would have to spend a valuable amount of time figuring the raga / notes of a song in order to be able to reproduce it.
For such artists, this application comes as a rescue. It uses Librosa a Python based library to identify the notes of a song and predict the raga of the song using machine learning models

This project leverages the use of scipy and Librosa library to transform, identify and generate the notes of any song. 
The application takes a song file, performs Fourier transform and converts it into series of frequency values. These values are then converted to notes using the functions of Librosa library. These notes are used to predict the raga of the song. The raga of the song, the heart of the project is predicted using a supervised machine learning algorithm which is built on a set of songs with unique ragas.

The application is hosted on flask server and apis have been created for different endpoints such as login, dashboard, notes generator, song manipulation and raga identification

## System Modules and Description
### Registration Page:
Users can register to the application by using the registration/signup page. Here the users can enter their username, email, and password in the form provided.
The app uses flask-security to bring security to user’s accounts. When a user registers for the first time, a post request is made to registration end point where the user’s password is hashed, a new unique id is generated and all the user’s details are stored in the database.
The unique id helps to generate a unique authentication token for the user, each time he/ she logins to the application

### Login Page:
Users can login to the application by using the login page. Here the users can enter their username, password in the form provided.
The app sends a fetch request to the endpoint login where flask-security checks for the username and password and sends back a token if the values match with the ones stored in the database.
Thereafter all requests to endpoints require this authentication token to verify if the user has signed in or not.
The authentication token is saved in the session storage of the application

### Dashboard:
Users logged in can view the dashboard once their authentication token has been validated. The dashboard brings interactivity to the application, by displaying songs and ragas found by the model 

### Graph and Notes Summary:
Users can visualize and get notes of the song they provide by using this     endpoint. This function uses matplotlib , scipy and librosa to generate frequencies, convert them using fourier transform, perform scaling, and converts it as notes.

### Raga Predictor:
This module is the heart of the application. It tries to map the notes of the song generated to raga using supervised machine learning algorithms and ensemble learning. It then displays the raga to the user and saves it in the database with other details

### Frontend:
The front end of the application leverages the Vue.js framework to utilize the advantages of JavaScript. The Vue.js fetches data using apis and then displays the response

### API endpoints have been created for the tasks mentioned

## How the model was built

•	First samples of songs with known Ragas were taken as a wave file.

•	These wave files were transformed into frequencies using Fourier transform.

•	Now the frequencies were sent to a function from Librosa library that converts signals to musical notes.

•	These notes were then converted to Carnatic notes.

•	A sample of the Carnatic notes were then picked for each song.

•	An Ordinal Encoder was used to convert the categorical variables to numbers from 0 to 12.

•	A list of ragas corresponding to each song was stored in a target variable.

•	The encoded samples and target variable was then sent to models like Random Forest and Logistic Regression. 

•	Both models gave a score of 87%. 

•	The model was pickled and saved into a .sav file for later user.

•	Thus when a new sample was sent for prediction, the sample was preprocessed in the above method and Raga was predicted.

•	The notes generated in the process is also shared with the user.

## Frameworks used

•	Python – Flask : 	Flask-restful |	Flask-security
  
•	Python – Librosa

•	Python – Scipy

•	SQLAlchemy

•	SQLite Database

•	Vue.js

## Screenshots

### Start Page
![image](https://user-images.githubusercontent.com/65553135/212360713-e74fc069-b263-41aa-8f2e-c3e390a9a4c0.png)

### Prediction Page
![image](https://user-images.githubusercontent.com/65553135/212360910-5d2de3c7-2beb-4646-8133-3d38515bf507.png)
![image](https://user-images.githubusercontent.com/65553135/212360933-734be37c-d561-46c1-866a-41eb686398bb.png)
![image](https://user-images.githubusercontent.com/65553135/212360956-74065257-fd5e-4526-b0b4-8a1ecc3b52ad.png)

### How it works
![image](https://user-images.githubusercontent.com/65553135/212361090-6f9c036a-4e36-43ff-9e5a-174063ecc9b4.png)

### Signup Page
![image](https://user-images.githubusercontent.com/65553135/212361834-7d39bba1-e2b1-4b6f-82ea-12df8ae2f4e2.png)

### Login Page
![image](https://user-images.githubusercontent.com/65553135/212361906-c8f822c9-b643-4b3c-a512-edd2545406f9.png)

### Dashboard
![image](https://user-images.githubusercontent.com/65553135/212361953-59b0acba-6a27-4a9f-9cb3-5bca708dda74.png)


 

