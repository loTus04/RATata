/////////////////////////////////
//Importation des librairies////
///////////////////////////////



var express = require('express');
var session = require('express-session');
var fs = require("fs")
var app = express();
var bodyParser = require('body-parser');
var morgan = require('morgan');
var ssn



/////////////////////////
//Lecture des donnees////
////////////////////////


const readBlogJson = fs.readFileSync('./data/blog.json');
var blog = JSON.parse(readBlogJson);



////////////////////////////////
//Definition des midlewares////
//////////////////////////////


app.use(bodyParser.json({limit: '10mb', extended: false}))
app.use(bodyParser.urlencoded({limit: '10mb', extended: false}))
app.use(express.static(__dirname + '/views'));
app.use(morgan('tiny'))
app.use(session({
    resave: true,
    saveUninitialized: true,
    cookie: {
        path: '/',
        httpOnly: false,
        maxAge: 24 * 60 * 60 * 1000
    },
    secret: '1234567890QWERT'
}));
app.set('view engine', 'ejs');



///////////
//Blog////
/////////






///////////////////////
//Creation de post////
/////////////////////



app.get('/create', (req, res) => {
   res.render("create")
});



app.post('/create', (req, res) => {


        blog.push({
            ID: blog.length + 1,
            Title: req.body.Title,
            Content: req.body.Content
        });
        fs.writeFileSync('./data/blog.json', JSON.stringify(blog, null, 4));
        res.redirect('/');
    
});



///////////////////
//Voir un post////
/////////////////



app.get('/posts/:id', (req, res) => {
    const {
        id
    } = req.params;
    let dataId;

    for (let dt of blog) {
        if (
            dt.ID === parseFloat(id)
        ) {
            dataId = dt;
            res.render('post', {
                dt: dt,
            });
        }
    }
});



//////////////////////
//Manager de Posts///
////////////////////



app.get('/', (req, res) => {
        const {
            filter
        } = req.query;
        let filterData = [];
        //Parametre de recherche
        if (filter) {
            for (let dt of blog) {
                if (
                    dt.Title === filter ||
                    dt.Content === filter ||
                    dt.ID === parseFloat(filter)
                ) {
                    filterData.push(dt);
                }
            }
        } else {
            //Selectionne toutes les donnees
            filterData = blog;
        }

        res.render('manage', {
            blog: filterData,
            filter,
        });
});



///////////////////////////
//Modification de posts////
/////////////////////////



app.get('/edit-post/:id', (req, res) => {
   
    const {
        id
    } = req.params;
    let dataId;

    for (let i = 0; i < blog.length; i++) {
        if (Number(id) === blog[i].ID) {
            dataId = i;
        }
    }

    res.render('edit-post', {
        blog: blog[dataId],
    });
});


app.post('/edit-post/:id', (req, res) => {
   
    const {
        id
    } = req.params; //parametres de la requete
    const {
        Title,
        Content,

    } = req.body;

    for (let i = 0; i < blog.length; i++) {
        if (Number(id) === blog[i].ID) {
            console.log(blog[i].Content)
            blog[i].Title = Title;
            blog[i].Content = Content;
        }
    }



    fs.writeFileSync('./data/blog.json', JSON.stringify(blog, null, 4));
    res.redirect('/');
});



///////////////////////////
//Suppression de posts////
/////////////////////////



app.get('/delete-post/:id', (req, res) => {
    
    var {
        id
    } = req.params; //parametre de la requete

    const newData = [];
    for (let i = 0; i < blog.length; i++) {
        if (Number(id) !== blog[i].ID) {
            newData.push(blog[i]);
            return res.redirect("/")
        }
        else res.redirect("/")

    }

    blog = newData;
    fs.writeFileSync('./data/blog.json', JSON.stringify(blog, null, 4));
    res.redirect('/');
});



///////////////////////
//Page Introuvable////
/////////////////////



app.get('*', function(req, res) {
    res.render('404');
});



///////////////////////////
//Lancement du serveur////
/////////////////////////



app.listen(process.env.PORT || 8080);
console.log('listening on port 8080');