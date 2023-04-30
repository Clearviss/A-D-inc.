import express from "express"
import cors from 'cors'
import review from './api/reviews.route.js'

const app = express()

app.use(cors())
app.use(express.json())

app.use("/api/v1/reviews", review)
app.use("*", (req, res) => res.status(404).json({error: "not found nigga"}))

export default app