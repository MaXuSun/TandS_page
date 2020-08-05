# Query System
This website consists of two parts: the front-end and the back-end. It uses the Django framework to handle the interaction between various data and uses the SQLite database to store all data in the back-end. It uses the Vue.js framework to render the data from the back-end in the front-end. The two parts will be introduced separately below.

![display](https://github.com/MaXuSun/TandS_page/blob/master/display_img.png)

# Frontend
## Requirement
```
node.js==12.18.2
vue-cli==4.1.1
vue==2.6.1
```

## Function
- Sign in and Sign up
- Choose system language
- Get schedule
- Switch account and Log out 
- Search for question
- Fuzzy search
- Upload a question
- Answer a question
- Check school policy and related regulations
- Get the contact information of the school
- Show hot topics


## Project setup
```
npm install
```
### Compiles and hot-reloads for development
```
npm run serve
```
### Compiles and minifies for production
```
npm run build
```
### Lints and fixes files
```
npm run lint
```

# Backend
## Requirement
```
nltk==3.4.5
gensim==3.8.1
Django==3.0.8
numpy==1.17.1
```

## Function
- Login
- Register
- Q&A search
- Add Question
- Answer Question

## run
`python manage.py runserver`
