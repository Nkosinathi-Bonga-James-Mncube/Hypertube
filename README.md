# Hypertube
What is  Hypertube?


Hypertube is a web application that allows the user to research and watch videos.The player will be directly integrated to the site, and the videos will be downloaded through the BitTorrent protocol.


Instructions

1 - Rename env.examples to .env and fill in neccessary details: (Remember no spaces after "=")

    EMAIL_HOST= // Email host eg.smtp.gmail.com
    EMAIL_HOST_USER=// Email address example@gmail.com 
    EMAIL_HOST_PASSWORD=//Email password
    API_KEY_IMDB=//Provide api code from http://www.omdbapi.com/
    API_KEY_THEMOVIEDB=//Provide api code from http://www.themoviedb.org/ 
    SOCIAL_AUTH_GOOGLE_OAUTH_KEY=//Provide code from https://console.developers.google.com/apis/credentials
    SOCIAL_AUTH_GOOGLE_OAUTH_SECRET=Provide api code from https://console.developers.google.com/apis/credentials
    SECRET_KEY=//Provide own Django secret key from settings.py new project created
    
2 - To run torrent client run "sudo qbittorrent-nox"


