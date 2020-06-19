- To switch databases, run the use statement. If the database doesn't already exist, it will be created:
```
use music
```
-  To insert data into collection. If the collection doesn't exist, it will be created:
```sh
db.artists.insert({ artistname: "The Tea Party" })
```

-  You can see the database in your list of databases by issuing the following command:
```sh
show databases
```

- You can also run the following line to view the contents of your database:
```sh
db.artists.+()
```

- You can also create collection using createCollection() method:
```sh
db.createCollection("producers")
```

- To create a collection with some options:
```sh
db.createCollection("log", { capped : true, size : 4500500, max : 4000 } )
```

- To see all the collections in the database:
```sh
show collections
```

- To insert multiple document in collection:
```sh
db.artists.insert(
   [
     { artistname: "The Kooks" },
     { artistname: "Bastille" },
     { artistname: "Gang of Four" }
   ]
)
```

- To insert embedded document in a collection:
```sh
db.artists.insert({
    artistname : "Deep Purple",
    albums : [
                {
                    album : "Machine Head",
                    year : 1972,
                    genre : "Rock"
                }, 
                {
                    album : "Stormbringer",
                    year : 1974,
                    genre : "Rock"
                }
            ]
})
```

- You can also use the insertOne() method to insert a single document into a collection:
```sh
db.musicians.insertOne({ _id: 1, name: "Ian Gillan", instrument: "Vocals" })
```

- As with insert(), you can insert embedded documents and arrays of documents:
```sh
db.artists.insertOne({
    artistname : "Miles Davis",
    albums : [
                {
                    album : "Kind of Blue",
                    year : 1959,
                    genre : "Jazz"
                }, 
                {
                    album : "Bitches Brew",
                    year : 1970,
                    genre : "Jazz"
                }
            ]
})
```

- To insert multiple documents you can use insertMany():
```sh
db.musicians.insertMany(
   [
     { _id: 2, name: "Ian Paice", instrument: "Drums", born: 1948 },
     { _id: 3, name: "Roger Glover", instrument: "Bass", born: 1945 },
     { _id: 4, name: "Steve Morse", instrument: "Guitar", born: 1954 },
     { _id: 5, name: "Don Airey", instrument: "Keyboards", born: 1948 },
     { _id: 6, name: "Jeff Martin", instrument: "Vocals", born: 1969 },
     { _id: 7, name: "Jeff Burrows", instrument: "Drums", born: 1968 },
     { _id: 8, name: "Stuart Chatwood", instrument: "Bass", born: 1969 },
   ]
)
```

- To insert many documents containing enbedded documents:
```sh
db.artists.insertMany(
[
{
    artistname : "Robben Ford",
    albums : [
                {
                    album : "Bringing it Back Home",
                    year : 2013,
                    genre : "Blues"
                }, 
                {
                    album : "Talk to Your Daughter",
                    year : 1988,
                    genre : "Blues"
                }
            ]
}, {
    artistname : "Snoop Dogg",
    albums : [
                {
                    album : "Tha Doggfather",
                    year : 1996,
                    genre : "Rap"
                }, 
                {
                    album : "Reincarnated",
                    year : 2013,
                    genre : "Reggae"
                }
            ]
}
])
```

- You can filter the results down by providing only the criteria that you're interested in:
```sh
db.artists.find({artistname: "The Tea Party"})
```

- To return musicians who play drums and where born before 1950:
```sh
db.musicians.find( { instrument: "Drums", born: { $lt: 1950 } } )
```

- To return musicians who play drums and where born after 1950:
```sh
db.musicians.find( { instrument: "Drums", born: { $gt: 1950 } } )
```

- To return musicians that either play drums or were born before 1950:
```sh
db.musicians.find(
   {
     $or: [ { instrument: "Drums" }, { born: { $lt: 1950 } } ]
   }
)
```

- To searching for all musicians who are either on vocals, or play guitar:	
```sh
db.musicians.find( { instrument: { $in: [ "Vocals", "Guitar" ] } } )
```

- To return only sepcific fields from document(projection) and ignore _id as it is returned by default:
```sh
db.musicians.find( { instrument: "Vocals" }, {_id: 0,  name: 1 } )
```

- To limit the documents to be returned. Will show only first 3 documents:
```sh
db.artists.find( { albums: { $exists: false }} ).limit(3)
```

- To skip a documents. It will skip the 1st & 2nd document and return the next 3 documents if exist:
```sh
db.artists.find( { albums: { $exists: false }} ).limit(3).skip(2)
```

- To return documents sorted as per their born date in ascending order:
```sh
db.musicians.find().sort({born: 1})
```

- The documents will be sorted by the first field specified, then the next, and so on:
```sh
db.musicians.find( ).sort( { instrument: 1, born: 1 } )
```