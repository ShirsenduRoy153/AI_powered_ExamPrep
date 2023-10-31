const Sequelize = require('sequelize');
const express = require('express');
const router = express.Router();

const { test } = require('../models');

router.get("/admin", async(req, res, next) => {
    res.render('admin')
})

router.post("/add_q", async(req, res, next) => {
    console.log(req.body)
    const q_id = req.body.q_id
    const q = req.body.q
    const o1 = req.body.o1
    const o2 = req.body.o2
    const o3 = req.body.o3
    const o4 = req.body.o4
    const a = req.body.a
    await test.create({ q_id, q, o1, o2, o3, o4, a })
    res.json({
        success: true,
        code: 200
    })
})

//-------Student----------//

router.get("/mcq-m", async(req, res, next) => {
    const tests = await test.findAll({
        raw: true
    })
    res.render('mcq-m', { title: 'mcq-m', tests })
})

router.post("/mcq-m_post", async(req, res, next) => {
    score = 0
    console.log(req.body.a)
    console.log(req.body.ak)
    if (req.body.a[0] == req.body.ak[0]) {
        score += 1
    }
    if (req.body.a[1] == req.body.ak[1]) {
        score += 1
    }
    if (req.body.a[2] == req.body.ak[2]) {
        score += 1
    }
    if (req.body.a[3] == req.body.ak[3]) {
        score += 1
    }
    if (req.body.a[4] == req.body.ak[4]) {
        score += 1
    }

    console.log("S C O R E = ", score)

    res.json({
        success: true,
        code: 200
    })
})

module.exports = router;