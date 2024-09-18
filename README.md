# MOVIE RECOMMENDER
This movie recommender recommends a list of movies based on a certain movie selected from the list of movies avaible. It considers the movie details like title, overview, genres, keywords etc of the movie chosen and returns a list of 20 movies that are much more similar, related or in the same category as the movie based on to recommend. The movies are returned in order of decreasing similarity from the most similar to less similar movie.
It is important to note that at the moment, the application can only give recommendation for a list of movies that are available in the search list.

You can check out the deployed application here-> [MOVIE_RECOMMENDER](#)
## AUTHORS
1. MAWEJJE MARK WILLIAM [LinkedIn](https://www.linkedin.com/in/mark-william-026649254/)
2. ZAINAB AKINOLA
3. BANDA WILLIAM

# INSTALLATION
To run the project, you just need to clone the repository to your local machine, install the dependencies as specified in the requirements.txt file. You also need to add this [similarity.pkl](https://drive.google.com/drive/folders/18HxpP7QrVubMMwI7osYuBuDmPIU19P9S) file in the root directory of the project or you can can specify an absolute path in the flask_app.py file where the 'similarity' file is loaded. The movies.pkl file can also be in the root directory of the project or its absolute path specified in the 'flask.py' file where it is loaded.
Following this simple installation procedure, you are ready to run the application

# USAGE
After installing all the app dependencies as applied in the requirements.txt file. Configure the sqlite3 database or any database of your choice since it will be used to store details of users using the application to signup, login to the application and also update their profile.
After configuring the database.
You can run the application by writing the command, 'flask run' in the console.
## EXPECTED OUTPUT
On successful fullfilling of all the requirements, the should be able to see the following page in your web browser:
### login page:
![Screenshot from 2024-09-18 21-16-16](https://github.com/user-attachments/assets/97d7e847-bdab-46b1-a379-eb61f88ca24a)

### home page:
![Screenshot from 2024-09-18 21-20-35](https://github.com/user-attachments/assets/9a7e5b4a-296e-4d6b-a21c-44cfa8cc20eb)

# CONTRIBUTING
Those interested in contributing to this project and make more advanced you can do the following:
1. Fork the repository
2. Create a new branch
3. Make changes and commit
4. Push to your branch
5. Open a pull request
If you find a bug or have a feature request, please [open an issue](https://github.com/Mark9Williams/MOVIE_RECOMMENDER/issues).

# RELATED PROJECTS
Here are some projects that are related or might be of interest:
1. [Movie-Recommendation-Flask-App](https://github.com/yukti99/Movie-Recommendation-Flask-App): This machine learning project is a Flask Web Application that uses collaborative item-to-item filtering to recommend suitable movies based on user’s rating of a previously watched movie.
2. [Recommender](https://github.com/AineshSootha/Recommender): The program allows the user to enter the title of the movie they have watched and choose what they liked about the movie. They may choose Genre , Cast or Collection. Each of these options prompts the program to call a different function. If the user chooses Genre, the program would return a list of movies with similar genres sorted according to the similarity of their summaries.

# LICENSING
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
