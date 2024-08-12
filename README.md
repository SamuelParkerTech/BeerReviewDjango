
![image](https://github.com/user-attachments/assets/62648137-b4b3-4a68-b282-a46e6d4732ba)
# The Carewfest Beer and Review Site

## Contents
- [About](#about)
- [Project Target](#Project-Target)
- [Agile](#Agile) 
- [Project Board](#Project-Board)
- [Live Deployment](#Live-Deployment)
- [Design](#Design)
- [Wireframes](#Wireframes)
- [ERD Designs](#ERD-Designs)
- [Database](#Database)
- [Features](#Features)
- [Testing](#Testing)
- [Validator Testing](#Validator-Testing)
- [Deployment via Heroku](#Deployment-Via-Heroku)
- [Future Features](#Future-Features)
- [Credits](#Credits)
- [Content Credit](#Content-Credit)
- [Technology](#Technology)-
- [Further Thoughts](#Further-Thoughts)

# About

The Carew Beer Review! 
A review of the beers at the yearly Carew Arms Beer Festival in Crowcombe in Somerset. A real ale festival with 18 different beers to try over the weekend. 

# Project Target

The website aims to address the need to review the beers at the recent beer festival at the Carew Arms in Somerset. There were 18 beers to taste over the course of a weekend. There were also ciders but the current scope is too only focus on the beers. 

The website will address this problem by providing separate options for each beer to read details of each beer and allow a user to leave a comment review and a score for each beer. The reviews will then be displayed alongside each beer on the beer page, and the score will also display on the card for each beer. 

The target audience for this website is largely attendees of the festival who were interested in rating the beers. However as the beers are also available in the wider public this could also be a resource for them to check and leave a comment for. Once created it could easily be adapted to be ready in time for next years festival, so that it can be updated during the weekend as well. 

# Agile

For the Agile process I utilised the Github project board and user stories. Detailing the production process and highlighting issues when they arose. 

![image](https://github.com/user-attachments/assets/368d3cab-91c4-4d83-8a47-f2592a0db5eb)

New user stories have been added as the project processed and based on user feedback during the final testing phase. 

A MOSCOW framework has been utilised. 

Mo: Full Beer Details, CRUD functionality.(Leave reviews, edit reviews, delete reviews)
S: Ratings that are shown on all pages and averaged. 
C: Code and style revisement. Future features such as Carousel view, ratings convered to star ratings. 
oW: Ability to add new beers as a user. This a specific website featuring specific beers at the festival, such a feature is thus not required. However, in future the site could be adapted for other beer festivals or personal reasons when having this ability would be beneficial. 

## Project Board

https://github.com/users/SamuelParkerTech/projects/8

# Live Deployment

Live Website - https://beereview-856687d00272.herokuapp.com/

# Design 

## Design Aims

The aim of the design is to make it really simple, clear and straightforward as to what the site is used for. A simple main landing page displaying the title with "CarewFest Beers & Reviews". A separate page for each beer containing further details and beers. In time, if project allows I would explore the option of having this pop up to keep the user on the same page.

The site does not encourage excessive drinking and is a means to share information on beers at the festival. I will include a link to https://www.drinkaware.co.uk/ to provide more information. 

Before the user accesses the page they will have to confirm they are 18 years old as the subject matter is age restricted (alcohol/beer). This will be created using a modal and will redirect the user away from the site if they click 'no'. 

## Main Page
 
The main page will host a selection of beers in bootstrap cards which are also links, hosted in a carousel so each beer can be moved between with clear arrows to enable this decision. By clicking on each beer the user will get more information and access to the reviews with an option to leave their own reviews. Each card will also display the rating of the beer (generated from user reviews). This design will remove screen clutter and make a pleasant viewing experience for the user. 

## Reviews Page

On the review page, further details on the beer will be displayed as well as the user rating again. If logged in users will be prompted to leave their own review, or log in to leave a review. The reviews will be displayed on this page underneath the further details, utlising more bootstrap cards to clearly display each separate review. I would like to display the score in a star format or a simple x/5 display. This display will be scrollable instead of a carousel format. The reviews will be split 3 to a row on large screens and 1/2 on smaller tablets & mobiles. Making sure that the remains responsive on all devices. It is possible that these review pages could be incorporated as pop ups if time allows but the main focus is on a working MVP at this time. 

## Fonts, Colours & Hero Image

I have selected font Oswald from Google Fonts as a clear and effective font. I've gone with a colour scheme of Orange & White matching the colours of the Beer Favicon seelected. 
C6A15B \
FFFFFF \
000000 \
Black will likely also be used. \
![image](https://github.com/user-attachments/assets/f3626b5f-ee8e-4479-8858-df968f2f53ba)

I have chosen a hero image of the exterior of the pub which will form the main background of the page. Image provided by Paul Savage of Out and About Images. 

# Wireframes 
## Modal - Alert Age Restriction

![Wireframes Chal18](https://github.com/user-attachments/assets/ee608557-a865-49ad-ba9d-9a0fd2b26b80)

## The main pages:

![Wireframes Main Page](https://github.com/user-attachments/assets/a876bcca-3202-4806-9541-149ecec53841)

## The review pages:

![Wireframes Review Pages](https://github.com/user-attachments/assets/d79cac2f-eed8-4a7a-99a0-2e41c418f0d0)

## Mock up of review page pop up:

![Wireframes Review Pop Up Version](https://github.com/user-attachments/assets/6a61f0a7-050e-42b5-8305-1a8730efa133)

# ERD Designs
For the ERD design I have used MIRO to create these. 

![image](https://github.com/user-attachments/assets/b2bf4dd6-06e0-4a6b-8848-cdc0b728d64f)

Live link to page: https://miro.com/welcomeonboard/SlV6RzNtRGxOU2JkRXRXVVQ2cXRXZHVBa0VrMnNiRlAweGdGUE5Qa3N1NEVLVWVVRGZYOXVZVExFaVg0RW9tU3wzNDU4NzY0NTg3NDg4NjQwODQwfDI=?share_link_id=241379904065

# Database

The main data for the database was created from the beers on offer at the beer festival. Once I had the list and images needed I added this data to a google sheet. I used ChatGPT to convert this data to in to a JSON form to save time. 

![image](https://github.com/user-attachments/assets/ba77e065-8963-4906-8a9e-348b92d83b22)

I also expanded the listings in order to match my ERD tables. The design of which were relatively fluid as during the creation process. I had a few issues during the loading of the data from posts.json due to changes to my model, a good lesson in making sure you know exactly what fields are required. In the end I had to manually remove the ratings table column and once that was sorted I was able to load the data successfully. 
![image](https://github.com/user-attachments/assets/82163a9e-aacb-4749-b673-7aae6bca5085)

# Features

# Age Verification
The main welcome page features a challenge ID age modal, if this is clicked no it redirects to google. It saves a cookie and will not display again for 30 days. 
![image](https://github.com/user-attachments/assets/27bb3219-6b35-4fdb-8aa3-a0d82f71621c)

# Main Page
Displays all beers, key details and the average review score. Each card is a link to the main beer page. These are highlighted when the mouse is moved over to indicate a link.

![image](https://github.com/user-attachments/assets/c5aa1e70-c1f7-41c5-b92d-596348ad9efa)

# Beer Details Page & Reviews
More details beer information, and separate review cards are displayed. A review form is at the bottom. \

![image](https://github.com/user-attachments/assets/402c3e6c-6d7b-4a59-8d14-99b2e2103f94)

The review form generates a score with a dropdown menu so figures outside of 1 - 5 cannot be added (When this was not a dropdown you would receive an error if a number higher than 5 was entered but it was not a good user experience). \
![image](https://github.com/user-attachments/assets/ff7b7e43-0f2b-4391-ae0b-e322ce648510)

On submit, edit and delete you receive a message confirming the action taken. Before deletion you are asked if you wish to confirm deletion by pop up modal. (Similar to the Age Verifcation). \
![image](https://github.com/user-attachments/assets/14f95eef-e68b-45d5-9e03-cbf5b918d432)
![image](https://github.com/user-attachments/assets/b30f88aa-985f-4d75-a2ed-87eb021ea944)
![image](https://github.com/user-attachments/assets/fa6c9751-1908-4e54-a357-56173a2ac043)
![image](https://github.com/user-attachments/assets/ab56fabb-2506-4b66-aea5-db509f311a0e)

## Sign In Page

![image](https://github.com/user-attachments/assets/29eb5d1d-60ae-4840-a061-31358456e938)

## Sign Up Page

![image](https://github.com/user-attachments/assets/7de67ef1-b85d-4ba5-9b1c-98639011316c)

## Logged In/Out
The user is displayed at the top right with a message "you are logged in as ..." as well as a link to log out. 
If no user is loggged in they are shown options Register, Login and "You are not logged in"

![image](https://github.com/user-attachments/assets/11487944-c6ca-41de-947b-3d36d4663a76)
![image](https://github.com/user-attachments/assets/3727d098-1995-49fc-9f1f-e06b7e13064d)

On log out they are asked if they wish to confirm logout. 
![image](https://github.com/user-attachments/assets/c427a0c2-0436-4a03-931e-72d2b0b45de4)

I checked responsiveness on other sites throughout the development process, I also used Am I Responsive for this. https://ui.dev/amiresponsive?url=https%3A%2F%2Fbytes.dev

![image](https://github.com/user-attachments/assets/23734750-7b54-458f-a04f-0da8b0667ac2)

## Django / Admin page 

![image](https://github.com/user-attachments/assets/0a99995b-a892-4dd5-b52b-47497a132435)

For users authentication I have used All Auth - https://docs.allauth.org/en/latest/installation/quickstart.html

# Testing

Testing was done both manually and using Validators (see next section).

## Known Bugs

There is currently a known issue where when editing the rating is removed rather than copied across in the dropdown. This should be filled in when you click edit based on the existing rating given. 
![image](https://github.com/user-attachments/assets/5b821dfe-4788-468f-bc8b-fca06ef1bf4b)
The Javascript is collecting the rating correctly but I have not been able to get it to set it correctly as of 12.08.2024. I have checked this by logging it to the console.
![image](https://github.com/user-attachments/assets/ddc2ebfa-f94c-4fdb-bedb-c762e48cb742)
If it is left blank, the updated review will not post and the user will get an error message "Review not updated" if they click update. 

On some pages you get a Javascript error TypeError: Cannot read properties of null (reading 'addEventListener')
    at HTMLDocument.<anonymous> (script.js:34:41).
This error relates to the age verification modal and only appears once the cookie is in place. 
Updated - I have removed this error by checking if the cookie is present and if so the code will exit. 12.08.2024

The Bootstrap Modals are still causing a few issues on the index page, from the Bootstrap css. 
![image](https://github.com/user-attachments/assets/ba7270b2-3a56-48aa-8e8f-dd6e17f565ab)

You can see in the Console log a quote from Douglas Adams Hitchhikers series, I added this to check Javascript was working in an early test period and have left it in as an easter egg.

# Validator Testing

I tested the HTML using W3 Validator using the URL checker function. https://validator.w3.org/
It does not like the google fonts in the head element, but this is how Google suggests adding them.
![image](https://github.com/user-attachments/assets/d13979c3-ad81-4cb0-acec-10dba9cd88a9)

CSS Validator testing used the jigsaw validator: https://jigsaw.w3.org/css-validator/ and posted no issues. 
![image](https://github.com/user-attachments/assets/23850db4-ef9c-460e-b265-dc8631ad85fa)

Javascript was testing using JS Hint: https://jshint.com/
The only errors are warnings about the use of ES6. ![image](https://github.com/user-attachments/assets/995f59b0-4094-477d-a971-e38cbdbc20a9)

Accessible Web testing currently leverages a score of 93/100
![image](https://github.com/user-attachments/assets/fd304eac-9e1d-4f82-ad09-1eb8163b8cb7)

# Deployment Via Heroku

First make sure the Debug is set to false \
![image](https://github.com/user-attachments/assets/e367bb35-3372-4c39-8672-5544cad9e9d8)

Connect your Github to your Heroku \
![image](https://github.com/user-attachments/assets/d8a7aed2-8c8e-4df5-92ce-286396be909f)

Make sure VARS are set correctly. \
![image](https://github.com/user-attachments/assets/cd552e8e-2fc9-4929-8f65-912860ec5c69)

In the deploy tab, scroll down and deploy MAIN Branch \
![image](https://github.com/user-attachments/assets/20234481-4a8a-44b7-9070-69b5bb1dd0c4)


# Future Features

I would like to add the functionality in future for the main page to be a carousel rather than a full page scroll. This would simplify the view and utilise less screen space. \
I would also like to make the review form accordion be closed on page load, and open when 'leave a review' or 'edit' buttons are clicked. 
In future efforts I would get the rating to load correctly when the edit button is used. (See known bugs).]

For a future functionality I would also like to add a user area, which would display previous reviews the user had left and a checkbox to tick off beers tried at the festival. If they have left a review it should automatically tick off a beer, likewise if they tick off a beer it should prompt them to leave a review.
![Wireframes FF User Area](https://github.com/user-attachments/assets/33b18c8b-0847-4f37-94c9-841549911dd9)


# Credits

# Content Credit

* Carew Pub Images courtesy of Out and Abouts Images https://www.outandaboutimages.co.uk/ \
* ChatGPT - Content Creation. Descriptions of some beers was tweaked with ChatGPT and some reviews were generated in this way. \
* Favicons - Favicon.io - https://favicon.io/emoji-favicons/beer-mug/
* FontAwesome - Social Icons https://fontawesome.com/

# Technology

* Github - Version Control & Project Kanban / Issues
* Gitpod - Code Editor
* Django - Python Framework
* BootStrap - CSS Framework
* Google Fonts - Oswald Font https://fonts.google.com/specimen/Oswald
* Miro - ERD Creation board https://miro.com/
* Coolors.co - Colour pallette/tone helper https://coolors.co/
* Google Sheets - Data collection & creation https://docs.google.com/spreadsheets/create
* Trello - Project Assessment Criteria Tracker https://trello.com/b/Gxg1ULD2/final-project-criteria
* AllAuth
* Am I Responsive https://ui.dev/amiresponsive?url=https%3A%2F%2Fbytes.dev

## Django Requirements

* asgiref==3.8.1
* cloudinary==1.40.0
* dj-database-url==0.5.0
* dj3-cloudinary-storage==0.0.6
* Django==4.2.14
* django-allauth==0.57.2
* django-summernote==0.8.20.0
* gunicorn==20.1.0
* oauthlib==3.2.2
* psycopg==3.2.1
* PyJWT==2.9.0
* python3-openid==3.2.0
* requests-oauthlib==2.0.0
* sqlparse==0.5.1
* urllib3==1.26.19
* whitenoise==5.3.0

# Further Thoughts

This project was a good learning experience. I had many issues which delayed me for a day or so while I worked out what the issues were. Sometimes these were as simple as typo, a misplaced comma, indent or simple logic not working. Many of these issues were because of a lack of experience. However, each issue helped me learn more about Django and how it works. Thus some problems once resolved, helped resolve other issues. For example, removing a column from my data table gave me the knowledge to add a column to my data table when the opposite issue arose. 








