
![SPMT Logo 1](https://github.com/user-attachments/assets/0319c37c-73f4-4b60-a55e-607e765b3a65)

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

# Project Board

https://github.com/users/SamuelParkerTech/projects/8

# Live Deployment

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

Live link to page: https://miro.com/welcomeonboard/SlV6RzNtRGxOU2JkRXRXVVQ2cXRXZHVBa0VrMnNiRlAweGdGUE5Qa3N1NEVLVWVVRGZYOXVZVExFaVg0RW9tU3wzNDU4NzY0NTg3NDg4NjQwODQwfDI=?share_link_id=241379904065

# Database

The main data for the database was created from the beers on offer at the beer festival. Once I had the list and images needed I added this data to a google sheet. I used ChatGPT to convert this data to in to a JSON form to save time. 

![image](https://github.com/user-attachments/assets/ba77e065-8963-4906-8a9e-348b92d83b22)

I also expanded the listings in order to match my ERD tables. The design of which were relatively fluid as during the creation process. I had a few issues during the loading of the data from posts.json due to changes to my model, a good lesson in making sure you know exactly what fields are required. In the end I had to manually remove the ratings table column and once that was sorted I was able to load the data successfully. 
![image](https://github.com/user-attachments/assets/82163a9e-aacb-4749-b673-7aae6bca5085)

# Features

The main welcome page features a challenge ID age modal, if this is clicked no it redirects to google. It saves a cookie and will not display again for 30 days. 

## Sign In Page

![image](https://github.com/user-attachments/assets/29eb5d1d-60ae-4840-a061-31358456e938)

## Sign Up Page

![image](https://github.com/user-attachments/assets/7de67ef1-b85d-4ba5-9b1c-98639011316c)

## Logged In

![image](https://github.com/user-attachments/assets/11487944-c6ca-41de-947b-3d36d4663a76)

## Django / Admin page 

![image](https://github.com/user-attachments/assets/0a99995b-a892-4dd5-b52b-47497a132435)

For users authentication I have used All Auth - https://docs.allauth.org/en/latest/installation/quickstart.html
# Testing

# Validator Testing

# Future Features

# Credits

# Content Credit

Carew Pub Images coutesy of Out and Abouts Images https://www.outandaboutimages.co.uk/ \
ChatGPT - Content Creation. Descriptions of some beers was tweaked with ChatGPT. \
Favicons - Favicon.io - https://favicon.io/emoji-favicons/beer-mug/ 

# Technology

* Github - Version Control & Project Kanban / Issues
* Gitpod - Code Editor
* Django - Python Framework
* BootStrap - CSS Framework
* FontAwesome - Social Icons
* Google Fonts - Oswald Font
* Miro - ERD Creation board
* Coolors.io - Colour pallette/tone helper
* Google Sheets - Data collection & creation
* Trello - Project Assessment Criteria Tracker
* AllAuth

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










