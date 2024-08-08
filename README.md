## Website for SGPA Calculation

### Aim
To host a website that calculates SGPA of a student given the scores of the student in all the subjects in that semester.

### Order of execution
1. Dowload the model.csv file.
2. Execute data.py
3. Execute app.py
Make sure to install the required packages & have a SQL database to store user information.

### Data
"model.csv" is the data file which contains the following details:
  - data = Grade points and SGPA of 1000 students.
  - X_data (independent data} = scores in {ML, DAA, DBMS, SI, DM,IoT, DBMS LAB, ML LAB}
  - Y_data {target data} = Corresponding calculated SGPA

###  Linear Regression Model
This section is dealt in "data.py" & the model is stored in "regression_model.pkl"
  - Data preprocessing involves splitting data into training and testing data in the ratio 80:20 ratio.
  - Inbuilt **LinearRegression()** model from **sklearn** module is used to train the data.
  - The trained model and its weights are stored in "regression_model.pkl" using **pickle** module.
  - The stored model can be loaded using pickle module whenever needed.

### Creating the website
This section is dealt in "app.py"
  - **Flask** helps integrate python code with html qhich is required to load the values entered through the        website in python variable, which will be sent as a parameter for model prediction.
  - Login page: 
      - Collects username & password.
      - All the existing user's details are stored in a SQL database.
  - Sign up page:
      - If a new user occurs, the sign up page is triggered.
      - Once the new user creates a username & password, it is stored in the database and he/she can login                through login page.
  - Model page:
      - Once the user has successfully logged in, the user is asked to enter grade points scored in             
        corresponding subjects.
      - Once submitted, the SGPA is printed on screen.
