# MBUA Unicorn Accelerator Dashboard

## Table of Contents

- [Table of contents](#Table-of-Contents)
- [About](#About)
- [Functionality/UX](#UX-Functionality-and-Navigation)
  - [UX](#UX)
  - [Functionality/Navigation](#Functionality-and-Navigation)
- [Technologies](#Technologies)
  - [Languages/Libraries](#Languages-Libraries)
  - [Other Resources](#Other-Resources)
- [Testing](#Testing)
  - [Tools and Methods Used for Testing](#Tools-and-Methods-Used-for-Testing)
- [Potential Enhancements](#Potential-Enhancements)
- [Deployment](#Deployment)
- [Credits](#Credits)
  - [Content](#Content)
  - [Acknowledgements](#Acknowledgements)

## About

Milestone Project Four / Full Stack Frameworks with Django / Code Institute

This is a web application is a dashboard for a fictitious company called MBUA that has created a product called Unicorn Accelerator (UA). This particular site is focussed on allowing customers to:
- Report bugs (issues) discovered in the UA product as well as track their progress.
- Upvote issues. If someone sees a bug entered by another customer that they too have seen with the product, they can come in here and upvote the 
- Request for enhancements to the UA product. When they request a feature/enhancement, they must put in a monetary bid. If the enhancement is accepted by MBUA, the customer must fill out credit card details and payment has to be accepted via the payment provider Strip before MBUA will commence work on the enhancement. The idea is that MBUA will take on feature requests from the highest bidder.

This application is also used by the administrator at MBUA:
- Viewing, acknowledging and closing issues
- Viewing, accepting, denying, and marking features complete.

## UX Functionality and Navigation

#### UX
- The web page is using one Google font:
1. **Montserrat**

- The primary colours are:
1. #4D7488 - all body text, a couple of h tags and active filter background
2. #007BFF (btn-primary) - Action buttons
3. #C4343B - Cancel buttons
4. #FFFFFF - button text

- Secondary colours:
1. #4EABDE - all links (except those in the copyright footer) and a couple of h tags

#### Functionality and Navigation

The site consists of the following pages that get be navigated to via the navbar:
1. Login
2. Registration
3. Profile
4. How it Works - this goes into detailed explanation as to how the application/site works. To that end, I am not going to put too much in here.
5. Landing Page - A brief overview here. Again, please see the "How it Works" page on the site for a detailed explanation. In short, this is the main dashboard page. It consists of 2 tabs: Issues and Features. You never have to leave the page to achieve the following:
- View issues via the Issues tab and view Feature requests from the via the feature requests tab. You do not have to be logged in to view this detail.
- Report an Issue
  - The report issue button is disabled if you are not logged in.
- Request a Feature
  - The request a feature button is disabled if you are not logged in.
- Upvote an issue
  - To upvote an issue you must be have an account and be logged in. Once you are logged in, expand the collapsible section (Show More) and click the thumbs up button
6. Credit card details and payment submission

Please see the "How it Works" page for much greater detail.


## Technologies

#### Languages and Libraries

- [HTML5](https://www.w3.org/TR/html5/ "HTML5 Official Site")
- [CSS3](https://www.w3.org/Style/CSS/ "Cascading Style Sheets Official Site")
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/ "JavaScript Official Site")
- [Python 3.6](https://www.python.org "Python Official Site")
- [Django 1.11.28](https://www.djangoproject.com "Django Official Site")
- [Bootstrap - v4.4.1](https://getbootstrap.com/docs/4.1/getting-started/introduction/ "Bootstrap Official Site")
- [jQuery v3.4.1](http://jquery.com/ "jQuery Official Site")
- [Font Awesome - v4](https://fontawesome.com/ "Font Awesome Official Site")
- [Stripe 2.43.0](https://stripe.com "Stripe Official Site")
- [SQLite3](https://www.sqlite.org "SQLite3 Official Site")
- [PostgresSQL 3.0.0](https://www.postgresql.com "PostgreSQL Official Site")


#### Other Resources

As always, for technical reference and help, I used the following sites.
- https://getbootstrap.com/
- https://www.w3schools.com/
- https://stackoverflow.com/
- https://https://docs.djangoproject.com/en/3.0/
- https://slack.com/

## Potential Enhancements

There is immense potential improvement of this site. Some that come to mind are:

- Sticky navbar. I tried and tried, but the way I have designed my navbar, I was getting bizarre behaviour. Normall I would work persevere but I am running out
of time to submit this project.
- A dynamic widget that appears as you scroll down the page that when clicked, will take you to the top
- Editting a feature or issue. That was the intention with having the issue and feature ids links -- it would bring that up in a form. Ran out of time.
- Allowing people to post comments and maintain a thread.
- Attaching documents to an issue or a feature request (screen shots, requirements documents, etc.)
- A stats page showing number of features added, issues closed etc.
- Blog and testimonials


## Testing

#### Tools and Methods Used for Testing

- [HTML Validation](https://validator.w3.org/ "W3C Markup Validation Service")
- [CSS Validation](http://jigsaw.w3.org/css-validator/ "CSS Validation Service")
- Chrome Developer Tools
- Django automated unit testing
- Travis CI
- Spreadsheet submitted with project was used as a checklist of all that was tested.


## Deployment

- Used GitHub Pages to deploy the final version (https://mrbrown2207.github.io/ms_iv_ua/).

## Credits

#### Content

- All written content is bespoke and created by the code author (Michael Brown).
- Photo images used are images that I purchased and have rights to use in any project.

#### Acknowledgements

- The Code Insititue! The tutors are always amazing, but were particularly helpful with this project. What 
made them really effective was there just would be some "chatting" between us and they would lead me to find 
the answer on my own. They acted like sounding boards. I really would like to single out Tim Nelson. I was 
working the weekends a lot on this and he was the one that was on duty. He knows his stuff, is patient, 
friendly and unbelievably encouraging.

