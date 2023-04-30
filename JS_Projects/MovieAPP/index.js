import app from "./server.js";
import mongodb from "mongodb"
// import ReviewsDA0 from "./dao/reviewsDA0.js"

const MongoClient = mongodb.MongoClient
const mongo_username = "domi500domi"
const mongo_password = "qf5VIhKlFQ0w198B"
const uri = `mongodb+srv://${mongo_username}:${mongo_password}@cluster0.2gaefcb.mongodb.net/test`

const port = 8000

MongoClient.connect(
    uri, {
        maxPoolSize: 50,
        wtimeoutMS: 2500,
        useNewUrlParser: true
    }
).catch(err => {
    console.error(err.stack)
    process.exit(1)
}).then(async client => {
    app.listen(port, () => {
        console.log(`listening on port ${port}`)
    })
})