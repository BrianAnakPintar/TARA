# T.A.R.A (The Amazing Rating Application)
### Notice:
Application is currently not being hosted due to financial concerns, therefore there is no live demo. Moreover, we removed settings.py from the repository as it contains sensitive information.

## What is this project?
This is a simple web application made during Grade 12 as a fun project which recreates https://www.ratemyprofessors.com/.com but implemented for a local high school. It is made using Django, and was hosted using DigitalOcean

# User workflow
### Logging in & Signing Up.
Upon using the site, users are asked to login or create a new account to proceed in accessing the site. Moreover, we require email authentication in order to avoid bots.

![login](https://github.com/BrianAnakPintar/TARA/blob/main/login-gif.gif)

### Reviewing a Teacher.
After gaining access, users are then allowed to choose which teacher they want to view reviews for, and whether they would like to review a teacher based on the given criterias. This will then update the teacher's ratings automatically.

![review](https://github.com/BrianAnakPintar/TARA/blob/main/review.gif)

### Removing a Review.
Sometimes user want to remove their reviews, here it's as simple as a click of a button. Upon removing, the ratings for the appropriate teacher should update automatically.

![remove](https://github.com/BrianAnakPintar/TARA/blob/main/remove.gif)

# Admin Perks
If you are a superuser or obtained the appropriate permissions, then visit `.../admin` and you will be able to see the admin dashboard from Django. Here you should be able to see, modify and add data onto the database appropriately. This allows easy access to adding new teachers onto the website, and modifying/removing reviews which may include inappropriate or offensive language.
