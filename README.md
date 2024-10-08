
![image](https://github.com/user-attachments/assets/37e38df3-6140-4c02-bec2-e68f62a3c0ba)

# The Carewfest Beer and Review Site

## Contents
- [About](#about)
- [Project Target](#Project-Target)
- [Agile](#Agile)
- [User Stories](#user-stories)
- [Project Board](#Project-Board)
- [Live Deployment](#Live-Deployment)
- [Design](#Design)
- [Wireframes](#Wireframes)
- [ERD Designs](#ERD-Designs)
- [Database](#Database)
- [Features](#Features)
- [Testing](#Testing)
- [Validator Testing](#Validator-Testing)
- [Accessibility](#Accessibility)
- [Deployment via Heroku](#Deployment-Via-Heroku)
- [Future Features](#Future-Features)
- [Credits](#Credits)
- [Content Credit](#Content-Credit)
- [Technology](#Technology)
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

Mo: Full Beer Details, CRUD functionality.(Leave reviews, edit reviews, delete reviews) \
S: Ratings that are shown on all pages and averaged.  \
C: Code and style revisement. Future features such as Carousel view, ratings convered to star ratings. \
oW: Ability to add new beers as a user. This a specific website featuring specific beers at the festival, such a feature is thus not required. However, in future the site could be adapted for other beer festivals or personal reasons when having this ability would be beneficial. 

# User Stories

User stories were used to keep track of the MOSCOW framework and project MVP as working through the project. 

![image](https://github.com/user-attachments/assets/c69ae848-3c81-4496-b457-c8c520faae10)

| User Story                                            | Detail                                              | Acceptance Criteria                                            |
|-------------------------------------------------------|-----------------------------------------------------|----------------------------------------------------------------|
| Review Accordion Auto Opens on click                  | As a user it would be clearer if the review box opened automatically when 'leave a review' or 'edit' buttons were clicked and it defaulted to closed.         | Responsive Accordion for the review table that opens on Leave a Review/Edit               |
| Carousel View                                         | As a user it would be nice to view the cards in a rotating carousel rather than scrolling the whole site.        | Cards display in a rotating carousel.          |
| From User Testing: Rating defaults to zero            | When I edit that review, the score defaults to 1 and I have to change it again. If the reviewer just wanted to edit the text, they might not realise they have to change the score again, so would be better if it could default to the score originally given.                      | When updating Edit Review the previous score should be set            |
| From live Tests: RFemove placeholder text             | Minor point, but when you click to add a review, the Review Title is already populated with the text "Review Title", which you have to delete. It would be nice if it was blank when you click in the field.      | Placeholder text should no longer appear in the fields.          |
| Can Edit & Delete Reviews                             | As a user I can edit my review and delete the review if required.      |  Edit function on related comments. Delete function on related comments.        |
| User can Create an account, login, and log out        | As a User I can create an account, log in to said account and log out of said account. | Users should successfully create accounts, log in, and log out. |
| Age Verification Only needs to be confirmed Once      | As a User I can Confirm my age once on the site so it does not constantly intefere.                 | Cookie accepted on modal age verification, No longer pops up.  |
| Create Drafts                                         | As a Super User/Admin I can create drafts ready to be posted.                               | Drafts can be created in the admin panel.                 |
| Create Posts                                          | As a Super User I can add posts so that site users can see beers at the festival.                   | Beer posts can be added/created in the admin panel.             |
| Active Feedback                                       | As a User I can see if I am logged in, when I post a comment or edit them so that I can keep track of my actions.    | I am told if logged in, Receive confirmation messages when comment is posted or edited. |
| Create Review/Beer Detail Page                        | Design beer detail and review pages                 | Beer detail page should display reviews and relevant information.|
| Age Restricted Content                                | As a User I can confirm I am over 18 so that I can review the age restricted content                     | A modal pop up querying my age before allowing access to content.If Yes to over 18 site access allowed. If no redirected away from site.
| User can leave a review                               | As a user I can leave a single review so that other users and me can know how I felt about a beer.              | I can leave a review for beers.              |
| View Beers                                            | As a User I can see all festival beers on the main page.           | A landing page with Beers to filter through. Clickable Beers with further details. Descriptive images/tasting notes and option to add reviews.                |


# Project Board

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

## About Page

A brief description of the pub, festival and website. This was a later addition as I had time to add.

## Fonts, Colours & Hero Image

I have selected font Oswald from Google Fonts as a clear and effective font. I've gone with a colour scheme of Orange & White matching the colours of the Beer Favicon seelected. 
C6A15B \ 
FFFFFF \
000000 \
Black will likely also be used. (Black has been used for text to increase contrast/visiblity) \
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

![image](https://github.com/user-attachments/assets/a1bba15b-9451-40c9-844e-ef676bd2d5c4)

# Beer Details Page & Reviews
More details beer information, and separate review cards are displayed. A review form is at the bottom. \

![image](https://github.com/user-attachments/assets/0f97527c-8f1e-4645-8f0d-e53cd44e9dfe)

The review form generates a score with a dropdown menu so figures outside of 1 - 5 cannot be added (When this was not a dropdown you would receive an error if a number higher than 5 was entered but it was not a good user experience). If you are not logged in you cannot leave a review \
![image](https://github.com/user-attachments/assets/d08a21d5-6f42-475f-a74a-3ebc0c44646a)
![image](https://github.com/user-attachments/assets/ff7b7e43-0f2b-4391-ae0b-e322ce648510)

On submit, edit and delete you receive a message confirming the action taken. Before deletion you are asked if you wish to confirm deletion by pop up modal. (Similar to the Age Verifcation). \
![image](https://github.com/user-attachments/assets/14f95eef-e68b-45d5-9e03-cbf5b918d432)
![image](https://github.com/user-attachments/assets/b30f88aa-985f-4d75-a2ed-87eb021ea944)
![image](https://github.com/user-attachments/assets/fa6c9751-1908-4e54-a357-56173a2ac043)
![image](https://github.com/user-attachments/assets/ab56fabb-2506-4b66-aea5-db509f311a0e)

## About Page

![image](https://github.com/user-attachments/assets/5371abfe-2154-4101-a77f-9bef79a2ccd6)

## Sign In Page

![image](https://github.com/user-attachments/assets/d1e02653-98a7-44c2-8c19-d770e0d05d16)

## Sign Up Page

![image](https://github.com/user-attachments/assets/46a8b0a9-871a-4581-bdee-18231e8ab17a)

## Logged In/Out
The user is displayed at the top right with a message "you are logged in as ..." as well as a link to log out. 
If no user is logged in they are shown options Register, Login and "You are not logged in" 

![image](https://github.com/user-attachments/assets/a9e59fae-daa9-4b65-98c9-199e5fc41187)
![image](https://github.com/user-attachments/assets/47e66916-8a51-41b3-9c40-506a3403de38)

Upon successful login a message is displayed. 

![image](https://github.com/user-attachments/assets/8981c22b-6f80-416c-bcee-872717346443)

On log out they are asked if they wish to confirm logout. \
![image](https://github.com/user-attachments/assets/c427a0c2-0436-4a03-931e-72d2b0b45de4)

Users who are not admins cannot access the admin page \
![image](https://github.com/user-attachments/assets/d77e75b7-1975-482e-802c-919b4dadca4e)

I checked responsiveness on other sites throughout the development process, I also used Am I Responsive for this. https://ui.dev/amiresponsive?url=https%3A%2F%2FBeeReviews.dev \
![image](https://github.com/user-attachments/assets/c0613e0f-b907-4e38-87eb-c49e6e43ec19)

## Django / Admin page 

![image](https://github.com/user-attachments/assets/0a99995b-a892-4dd5-b52b-47497a132435)

For users authentication I have used All Auth - https://docs.allauth.org/en/latest/installation/quickstart.html

# Testing

## Focus Group Testing

Before going live the site was made available to a small group of attendees to the beer festival to gather feedback on design, check for issues and test bugs. This feedback was incorporated and added to the site/user stories. 

| Feedback                        | Action                          | Outcome                        |
|----------------------------------|---------------------------------|--------------------------------|
| I just added a review for Exmoor Beast. On the homepage, the rating appears. But when I click on Exmoor Beast, the Rating shows as "No ratings yet" -   | Code error resulting in rating not displaying correctly fixed | Review rating is correctly displayed |
| Minor point, but when you click to add a review, the Review Title is already populated with the text "Review Title", which you have to delete. It would be nice if it was blank when you click in the field.        | Placeholder text removal added to User Stories and code edited to remove the fixed placeholder text | Placeholder text is now automatically removed  |
| The review I left was 5/5 for the beast (obvs). When I edit that review, the score defaults to 1 and I have to change it again. If the reviewer just wanted to edit the text, they might not realise they have to change the score again, so would be better if it could default to the score originally given. | Added to User Stories - Score defaults to 1 on editing | Currently a known bug which remains in development for a future update  |

## Manual Testing

In the process of testing I created the a test account "testaccount" for the purposes of checking the functionality of the site. In this process, I was able to add reviews, edit reviews and delete them. Full testing details can be found below. 

### Site Navigation / UX

| **Test** | **Expected Outcome** | **Result** | **Action Taken** |
|---|---|---|---|
| Age Verification Modal Site Load |  Age Verification Modal Pops Up |  Pass | None |
| Age Verication Modal Saves cookie if Yes| Cookie Saved - Check if Cookie stops Modal loading (see below)| Pass | None |
| Age Verification Redirects on No|Page redirects to Google| Pass| None |
| Age Verifcation Modal does not load if cookie present | Site loads with no Modal | Pass | None | 
| Beer Page Links | Beer Card link goes to the correct beer page | Pass | None |
| About Page Link | About Page loaded | Pass | None|
| External Links | External Links Open to New Windows / Correct Sites | Pass | None |
| Beer Ratings Main Page | Beer Rating is displayed in star format OR if no reviews are yet left "No ratings yet" | Pass | None |
| Beer Ratings Details Page |  Beer Rating is displayed in star format OR if no reviews are yet left "No ratings yet" | Pass | None |

#### If Not Logged In

| **Test** | **Expected Outcome** | **Result** | **Action Taken** |
|---|---|---|---|
| Log in Status| 'You are not logged in' displays in Nav Bar | Pass| None |
| Register Link | Opens Register page| Pass | None |
| Login Link | Opens Login page | Pass | None |
| Register Account | Account is registered, message stating account registered | Pass | None |
| Register Account Incorrect | Account is NOT created due to incorrect details | Pass | None |
| Login | Login is successful,  Message stating you are logged in | Pass | None |
| Add/Edit Reviews | Prompted to Log in to leave a review / cannot edit reviews | Pass | None |

### CRUD Functionality

### If Logged In

| **Test** | **Expected Outcome** | **Result** | **Action Taken** |
|---|---|---|---|
| Log in Status | 'You are logged in' displays in Nav Bar | Pass| None |
| Login / Register / Logout | Logout button should display, Register/Login options are hidden | Pass | None |
| Add Reviews | Can add reviews to beers | Pass | None |
| Review correct | All necessary fields completed or throws error/review not posted | Pass | None |
| Edit Own Reviews | Can edit their own reviews | When editing the score resets to blank, they cannot complete the review without setting the score so need to reset it. | This SHOULD keep the original score but it currently does not work as such, making it force them to rescore is a work around to avoid it resetting to 1 - see known bugs below. NOW RESOLVED|
| Delete Own Reviews | Delete own reviews and not others | Pass |
| Delete confirmation | When deleting a review a pop asks "Are you Sure, this action cannot be undone" | Pass | None |
| Logout | Log out confirmation screen, and confirm account is logged out message once confirmed | Pass | None |

## Admin Page

| **Test** | **Expected Outcome** | **Result** | **Action Taken** |
|---|---|---|---|
| Login as Super User/Admin | Login Opens Admin Page | Pass | None |
| Login as Standard User | Unable to login | Pass | None |
| Add New Beer | Can Add New Beer Details | Pass | None |
| Edit Pages | Can edit pages / Reviews | Pass | None |
| Delete | Can Delete Page / Reviews | Pass | None |

Leaving a review test \
![image](https://github.com/user-attachments/assets/a25817b1-77ed-4b34-98e6-b6160204899d) \
Edit/Delete own review function test \
![image](https://github.com/user-attachments/assets/3679046e-130b-4851-8222-c8222adc70d1) \
Edited review test outcome(edited review) \
![image](https://github.com/user-attachments/assets/58c3d9f5-dacc-4896-9936-6bc8e6b7dc55) \
Delete review pop up test \
![image](https://github.com/user-attachments/assets/0c3c996a-812a-408e-b99c-e3edbfbee8d0) \
Deleted review message confirmation test \
![image](https://github.com/user-attachments/assets/28217628-0793-4aae-8b36-ab8a161305ae)


## Known Bugs

There is currently a known issue where when editing the rating is removed rather than copied across in the dropdown. This should be filled in when you click edit based on the existing rating given. 
![image](https://github.com/user-attachments/assets/5b821dfe-4788-468f-bc8b-fca06ef1bf4b)
The Javascript is collecting the rating correctly but I have not been able to get it to set it correctly as of 12.08.2024. I have checked this by logging it to the console.
![image](https://github.com/user-attachments/assets/ddc2ebfa-f94c-4fdb-bedb-c762e48cb742)
If it is left blank, the updated review will not post and the user will get an error message "Review not updated" if they click update. 

### Bug Updated 07.10.2024
This is now resolved. I believe the issue was due to converting the rating to a star system so it was not pulling the original score. I have thus added code to the HTML and Javascript to make sure the right number is requested. It is now working as intended as evidenced by the Print to console function.

![image](https://github.com/user-attachments/assets/9e08980a-75ca-4c06-a6cb-d4e68612af43)
![image](https://github.com/user-attachments/assets/50067559-13ee-4831-8c3a-dadb6c8e02c3)
![image](https://github.com/user-attachments/assets/07995f24-606b-44c4-bfab-6e9a672436a2)
![image](https://github.com/user-attachments/assets/fcc89be0-df60-4cb6-b9ee-7cfb34e25f86)


On some pages you get a Javascript error TypeError: Cannot read properties of null (reading 'addEventListener')
    at HTMLDocument.<anonymous> (script.js:34:41).
This error relates to the age verification modal and only appears once the cookie is in place. 
Updated - I have removed this error by checking if the cookie is present and if so the code will exit. 12.08.2024


The Bootstrap Modals are still causing a few issues on the index page, from the Bootstrap css. 
![image](https://github.com/user-attachments/assets/ba7270b2-3a56-48aa-8e8f-dd6e17f565ab)

You can see in the Console log a quote from Douglas Adams Hitchhikers series, I added this to check Javascript was working in an early test period and have left it in as an easter egg.

# Validator Testing

## HTML
I tested the HTML using W3 Validator using the URL checker function. https://validator.w3.org/
![image](https://github.com/user-attachments/assets/fbf51967-ee58-4c74-b293-01119e77fe0e)
![image](https://github.com/user-attachments/assets/04147cea-0468-474f-9ede-770470ed6c79)
![image](https://github.com/user-attachments/assets/91bffdb3-4d95-4013-a4f5-42ab8e75813d)

## CSS
CSS Validator testing used the jigsaw validator: https://jigsaw.w3.org/css-validator/ and posted no issues. 
![image](https://github.com/user-attachments/assets/23850db4-ef9c-460e-b265-dc8631ad85fa)

## Javascript
Javascript was testing using JS Hint: https://jshint.com/
Two undeclared variables 'Bootstrap' which is part of the modal process. This is fixed by adding /* Global Bootstrap */ to the file. 
![image](https://github.com/user-attachments/assets/7a5edf10-6a98-4c7f-8af1-e497478f9cae)


## Python PEP 8 CI Checker - https://pep8ci.herokuapp.com/
### About Testing
models.py ![image](https://github.com/user-attachments/assets/bbdcb5b7-4d34-4cb3-8b18-665857965d24)
admin.py ![image](https://github.com/user-attachments/assets/1a33b85c-07aa-456d-8cbe-e8c79ddfdd60)
apps.py ![image](https://github.com/user-attachments/assets/64d9ba5e-054b-4cbf-beae-4cd25b5cc288)
urls.py ![image](https://github.com/user-attachments/assets/457bab58-8416-4355-b836-0d373f4fd179)
views.py ![image](https://github.com/user-attachments/assets/df6cb41d-e99d-4090-95ca-2364c7a60c95)

### Beer_Card Testing
Custom_Filters.py ![image](https://github.com/user-attachments/assets/116a1db5-a95b-42bf-9136-59c4d4eaae17)
admin.py ![image](https://github.com/user-attachments/assets/c068769b-5f34-41c3-8633-08b3d52b9bcf)
apps.py ![image](https://github.com/user-attachments/assets/d072c237-9b61-4a26-9da3-aeef57cf1d40)
forms.py ![image](https://github.com/user-attachments/assets/c0b8bd08-3710-45a8-89a4-fec26f2ed996)
models.py ![image](https://github.com/user-attachments/assets/b0d0c266-b2d6-4e67-8f13-c3ef76a52ae3)
urls.py ![image](https://github.com/user-attachments/assets/e64e244b-a3a0-4b6f-a33d-bf19f57f3e75)
views.py ![image](https://github.com/user-attachments/assets/422a8815-7616-4df8-9a5e-baeb4699405e)


### BeeReview Testing
asgi.py ![image](https://github.com/user-attachments/assets/619d28ad-c351-46d3-bbe2-1b655fc18c16)
settings.py (lines too long errors from Django creation) ![image](https://github.com/user-attachments/assets/7fa5860f-92ab-460b-8121-6b7887c4d040)
![image](https://github.com/user-attachments/assets/8fc53544-a16f-4727-974f-71eb766d0ac4)
urls.py ![image](https://github.com/user-attachments/assets/63e8d14e-4f6c-436a-b297-855f52b08543)
wsgi.py ![image](https://github.com/user-attachments/assets/8b7b7100-26b0-49f7-9bd6-0676865d48c5)


# Accessibility
In checking contrast a lot of the text was failing/posting a warning in Chrome Dev tools, I changed most the text to black and it now scores highly in contrast. \
![image](https://github.com/user-attachments/assets/9ec3664a-2cae-4882-a28a-09a5afbe694d)


Accessible Web testing currently states no accessibility issues (WCAG)
![image](https://github.com/user-attachments/assets/7d3a8708-cc45-4b81-8da0-4cdca88c6fac)

## Lightouse Testing

![image](https://github.com/user-attachments/assets/887e3c03-0121-4ddd-84ea-31b250dcf235)

I score lowest on 'best practices' - this is because Cloudinary is sending cookies with the images. \
![image](https://github.com/user-attachments/assets/3a3afc22-e9e3-48e1-9cf0-789e9a33c03c)
![image](https://github.com/user-attachments/assets/96e0011b-60c2-48c6-87cd-75528f0a7055)


# Deployment Via Heroku

First make sure the Debug is set to false \
![image](https://github.com/user-attachments/assets/e367bb35-3372-4c39-8672-5544cad9e9d8)

Connect your Github to your Heroku \
![image](https://github.com/user-attachments/assets/d8a7aed2-8c8e-4df5-92ce-286396be909f)

Make sure VARS are set correctly. \
![image](https://github.com/user-attachments/assets/cd552e8e-2fc9-4929-8f65-912860ec5c69)

In the deploy tab, scroll down and deploy MAIN Branch \
![image](https://github.com/user-attachments/assets/20234481-4a8a-44b7-9070-69b5bb1dd0c4)

## Detailed DJango/Heroku Set Up Instructions

| **Step** | **Code** | 
|---|---|
| **In Github** |
| Create a new Github Repo | Github > new Repository |
| Open Repo | If your Github is utlising the plugin click 'Open' to launch your preferred IDE |
| **In IDE**|
| Install Django: | pip3 install Django~=4.2.1 |
| Create requirements file | pip3 --local > requirements.txt |
| Create Project (proj_name)| Django-admin startproject proj_name . |
| Run Server | python3 manage.py runserver |
| Add Servers to ALLOWED_HOSTS in settings.py | ALLOWED_HOSTS = ALLOWED_HOSTS = ['.codeinstitute-ide.net', '.herokuapp.com'] |
| Create App (app_name) | python3 manage.py startapp app_name |
| Add to INSTALL_APPS in settings.py | INSTALLED_APPS = [… 'app_name',] |
| **Set Up Heroku** |
| Heroku Dashboard | https://www.heroku.com/ |
| Create new Heroku App | Choose unique name / select close region |
| Add Config Vars | Config Vars > Reveal Config Vars > Add New Key > DISABLE_COLLECTSTATIC value 1 |
| **In IDE** |
| Install web server Gunicorn and freeze | pip3 install gunicorn~=20.1 \ pip3 freeze --local>requirements.txt |
| Create Procfile | create Procfile in root directory |
| Declare Procfile | Add web : gunicorn proj_name.wsgi in Procfile |
| **In Heroku** |
| Connect Repository | Navigate to Deploy tab > connect to Github Repo |
| Check Add ons & Dynos | Inside app resources make sure to use Eco Dynos. Delete PostGres DB Add-ons |
| **Database** |
| Create Postgres Database | CI Database Creator - https://dbs.ci-dbs.net/ |
| **In IDE** |
| Install Database Packages | pip3 install dj-database-url~=0.5 psycopg / then pip3 freeze --local > requirements.txt |
| Create env.py file | Root directoy add env.py and add to .gitignore |
| **In env.py** |
| import OS | Top line 'import os' |
| set enviroment variables | os.environ["DATABASE_URL"] = "Paste in PostgreSQL database URL" |
| Secret Key | os.environ["SECRET_KEY"] = "Make up your own randomSecretKey" |
| **In Heroku** | 
| Add Secret Ket to config Vars |  SECRET_KEY, “randomSecretKey” |
| Add a Config Var called DATABASE_URL | DATABASE_URL, “yourDBUrlgoeshere” |
| **In settings.py** |
| Link to env.py | from pathlib import Path, import os, import dj_database_url, if os.path.isfile("env.py"): import env |
| Remove secret key | SECRET_KEY = os.environ.get('SECRET_KEY') |
| Comment out old Database section | # DATABASES = { } ( # on each line ) |
| Add new Databases section | DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} |
| **Migrate Database** |
| Save all files and Migrate | python3 manage.py migrate |
| **Create Super User** |
| Create Super User | python3 manage.py createsuperuser |
| **In settings.py** |
| Set DEBUG to false | DEBUG = False |
|**Redeploy** |
| Push all Git changes and commits | Redeploy to Heroku |

The project should now be ready to begin

# Future Features

I would like to add the functionality in future for the main page to be a carousel rather than a full page scroll. This would simplify the view and utilise less screen space. \
I would also like to make the review form accordion be closed on page load, and open when 'leave a review' or 'edit' buttons are clicked. \
In future efforts I would get the rating to load correctly when the edit button is used. (See known bugs). \
Another feature I would like to add would be to display the beers / reviews in order of rating as well as by name, or grouped by brewery. \

For a future functionality I would also like to add a user area, which would display previous reviews the user had left and a checkbox to tick off beers tried at the festival. If they have left a review it should automatically tick off a beer, likewise if they tick off a beer it should prompt them to leave a review.
![Wireframes FF User Area](https://github.com/user-attachments/assets/33b18c8b-0847-4f37-94c9-841549911dd9)


# Credits

## Content Credit

* Carew Pub Images courtesy of Out and Abouts Images https://www.outandaboutimages.co.uk/ 
* ChatGPT - Content Creation. Descriptions of some beers was tweaked and some site descriptions were created with ChatGPT 
* Favicons - Favicon.io - https://favicon.io/emoji-favicons/beer-mug/
* FontAwesome - Social Icons https://fontawesome.com/
* All other images provided by S Parker Photography www.sparkerphotography.co.uk
* Django set up using the CodeStar blog tutorial and Django Setup and Deployment Guidebook supplied by David Calikes and Code Institute.
* Troubleshooting - Django Documentation, Bootstrap Documention, Stack Overflow, Google and ChatGPT were also used when issues arose. 

## Technology

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
* Am I Responsive https://ui.dev/amiresponsive?url=https%3A%2F%2FBeeReviews.dev

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








