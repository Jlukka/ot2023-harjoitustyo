# ohjelma
(roguelite?) pakanrakennus peli
## kuvaus
(roguelike elementtejä) hyödyntävä pakanrakennuspeli jossa pelaaja siirtyy kartalla olevien paikkojen läpi kohti päävihollista samalla muokaten pakkaansa. jokaisessa taistelussa vihollinen pyrkii tappamaan pelaajan, pelaaja pelaamalla kortteja pyrkii tappamaan vihollisen. vihollinen seuraa jotain yksinkertaista logiikkaa eikä pelaa kortteja. 
## perusversion toiminnallisuus
- pelaaja on kartalla jossain paikassa
    - kartta on perusversiossa lineaarinen ja sama joka pelikerralla
- pelaajalla on  aloituskorttipakka [x]
- pelaajan siirtyessä taisteluun taistelu  [x]
    - pelaaja saa satunnaisesti jonkun määrän kortteja pakastaan [x]
    - pelaaja voi pelata kädessään olevia kortteja
        - korteilla on jokin efekti esim tekee vahinkoa viholliseen tai parantaa pelaajaa
    - vihollisen elämäpisteiden loppuessa pelaaja voittaa
    - pelaajan elämäpisteiden loppuessa pelaaja häviää
- pelaajan siirtyessä kauppaan pelaaja voi joko ostaa kortteja tai poistaa kortin pakasta
- käyttäjä voi tallentaa pelinsä
- käyttäjä voi ladata pelinsä
- käyttäjän pelatuista peleistä tallentuu tietoa joka on nähtävillä
- käyttäjä voittaa tappaessaan kartan lopussa olevan päävihollisen
## jatkokehitysideat
- useampi päävihollinen
- erilaisia paikka tyyppejä
- erilaisia tavaroita joita pelaaja voi saada?
    - tavaroita voisi saada vahvemmista kuitenkin päävihollista heikommista vihollisista
    - tavarat voisivat antaa bonuksia erilaisista asoista riippuen
- satunnaisesti generoitu kartta
- enemmän vihollistyyppejä
- enemmän kortteja
- mahdollisuus vaihtaa pakkaa (muuttaa kaikki kortit joita voi saada pelin aikana ja aloituspakan)
- vaikeustason lisäys?
    - muuttaa vaikeutta jollain näkyvällä tavalla
        - nostaa vihollisten elämäpisteitä
        - vähentää pelaajan elämäpisteitä
        - poistaa tietyn vihollistyypin 
        - muuttaa jonkin kortin vahvuutta