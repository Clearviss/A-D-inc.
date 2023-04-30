import mongodb from "mongodb";
const ObjectID = mongodb.ObjectID

let reviews

export default class ReviewsDA0 {
    static async injectDB(conn) {
        if (reviews) {
            return
        }
        try {
            reviews = await conn.db("reviews").collection("reviews")
        } catch(e) {
            console.error(`Unable to establish connection handles in user DAO: ${e}`)
        }
    }


    static async addReview(movieId, user, review) {
        try {
            const reviewDoc = {
                movieId: movieId,
                user: user,
                review: review,
            }

            return await reviews.insertOne(reviewDoc)
        } catch (e) {
            console.error(`unable to post review: ${e}`)
            return {error: e}
        }
    }

    static async getReview(reviewId) {
        try {
           return await reviews.findOne({_id: ObjectId(reviewId)})
        } catch (e) {
           console.error(`Unable to get review: ${e}`)
           
        }
    }
}