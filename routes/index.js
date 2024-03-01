const Sequelize = require('sequelize');
const express = require('express');
const router = express.Router();

const { test } = require('../models');
const { status } = require('../models');

//-----------------------Future Use-----------------------//
// const { type } = require('os');
// const { resolve } = require('path');

const { spawn } = require('child_process');

function runPythonFunction(topic, marks) {
    if (typeof topic !== 'string' || typeof marks !== 'string') {
        return Promise.reject(new Error('Invalid topic or marks'));
    }
    return new Promise((resolve, reject) => {
        const pythonProcess = spawn('python', ['python/graph.py', topic, marks]);
        let output = '';

        // Capture the standard output
        pythonProcess.stdout.on('data', (data) => {
            output += data.toString();
        });

        // Capture the standard error
        pythonProcess.stderr.on('data', (data) => {
            console.error(`Python error: ${data}`);
            reject(data.toString());
        });

        // Handle process completion
        pythonProcess.on('close', (code) => {
            if (code === 0) {
                console.log("Python script output:", output.trim());
                resolve(output.trim());
            } else {
                console.error(`Python process exited with code ${code}`);
                reject(`Python process exited with code ${code}`);
            }
        });
    });
}


//-------------------------------------------------X-------------------------------------------------//

//ADMIN PANEL
router.get("/admin", async(req, res, next) => {
    res.render('admin')
})

//ADD QUESTIONS
router.post("/add_q", async(req, res, next) => {
    console.log(req.body)
    const q = req.body.q
    const o1 = req.body.o1
    const o2 = req.body.o2
    const o3 = req.body.o3
    const o4 = req.body.o4
    const a = req.body.a
    const t = req.body.t
    await test.create({ q, o1, o2, o3, o4, a, t })
    res.json({
        success: true,
        code: 200
    })
})

//HOME
router.get("/", async(req, res, next) => {
    const statuses = await status.findOne({
        where: { id: 1 }
    })
    res.render('home', { title: 'home', statuses })
})

//MCQ PANEL
router.get("/mcq", async(req, res, next) => {
    const statuses = await status.findOne({
        where: { id: 1 }
    })
    topic = statuses.currenttopic
    const tests = await test.findAll({
        where: { t: topic }
    })
    res.render('mcq', { title: 'mcq-m', tests, topic })
        //Exception Your Course is completed...
})

// router.get("/mcq-m/:topic", async(req, res, next) => {
//     console.log(req.params.topic)
//     const tests = await test.findAll({
//         where: { t: req.params.topic }
//     })
//     res.render('mcq-m', { title: 'mcq-m', tests, topic })
//         //Exception Your Course is completed...
// })

marks = 0

//SCORE CALCULATION
router.post("/mcq_post", async(req, res, next) => {
    console.log(req.body.t)
    console.log(req.body.a)
    console.log(req.body.ak)
    if (req.body.a[0] == req.body.ak[0]) {
        marks += 1
    }
    if (req.body.a[1] == req.body.ak[1]) {
        marks += 1
    }
    if (req.body.a[2] == req.body.ak[2]) {
        marks += 1
    }
    if (req.body.a[3] == req.body.ak[3]) {
        marks += 1
    }
    if (req.body.a[4] == req.body.ak[4]) {
        marks += 1
    }

    console.log("S C O R E = ", marks)
    const result = marks

    await runPythonFunction(req.body.t[0], marks.toString());


    marks = 0

    res.json({
        success: true,
        code: 200,
        result: result,
    });
})

router.get("/doc/:name", async(req, res, next) => {
    res.render('doc', { title: 'doc' })
})

router.get("/progress", async(req, res, next) => {
    res.render('progress', { title: 'progress' })
})

module.exports = router;