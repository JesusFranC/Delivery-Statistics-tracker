#   Delivery Statistics Data Tracker Project

A WIP tracker for collecting and organizing personal data from gigs like Uber Eats and door dash

##  Why?

As a student, my schedule has been a bit hectic, so I picked up Uber Eats as a part time gig

The thought occurred to me, that it should be possible to make a program that helps me optimize what times and areas I should be working, so I can reduce downtime and be more efficient with my time.

## The Goal

My current goal is to be able to be able to collect all trips and details from them in a way that can be accessed and read by other programs, and can be read by humans

~~My progress on this program is going to be split in three parts~~

~~- The Data Collection API:
    - This involves creating a set of functions that allow me to add, remove, and manipulate data from my trips. 
    - I do not have access to any API's that would allow me to automate this, so it will be all manual in the meantime~~

~~- Data Proccessing:
    - Using data collected from the previous part, and analyzing it in such a way to recognize patterns
    - The end goal is to return real information on what times, locations, and dates would be optimal to be work~~

~~- The GUI:
    - The final part that would tie the previous two together in a way that is user friendly and easy to work with. 
    - It would provide an interface with all the functionality of the previous two parts combined~~

I am rethinking the roadmap of this project based on recent experience in my senior project for school. Rather than a mobile app, I have decided that a RESTful API style app would be more applicable for my use case

- Architecture
    - The app will be a Single Page Web Application (SPWA)
    - Security will be integrated into every microservice individually, as they will all share a joint security library
    - I will be using an MVC Style archictecture The back end will not be generating any views/HTML, the task will be delegated entirely to the front end

- Back end
    - The backend will be written in C# using the ASP.NET Core Library
    - The backend will be created with an MVC style architecture, where each individual service will have a dedicated controller

- Front end
    - The frontend will be written in Java using the React.js Library
    - The front end will be responsible for creating the views and dynamically adjusting as users interact with the platform

## Progress
- Because I am rethinking the main architecture of the application, I am moving back to where I started. However, I do have a set of pre-existing applicable libraries from a prior project I will be transferring over.
