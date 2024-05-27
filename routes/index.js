const Sequelize = require('sequelize');
const express = require('express');
const router = express.Router();

const { test } = require('../models');
const { status } = require('../models');

const { spawn } = require('child_process');

//PYTHON
//PYTHON
//PYTHON
function TestMCQ(topic, marks) {
    if (typeof topic !== 'string' || typeof marks !== 'string') {
        return Promise.reject(new Error('Invalid topic or marks'));
    }
    return new Promise((resolve, reject) => {
        const pythonProcess = spawn('python', ['python/graph.py', topic, marks]);
        let output = '';

        // Capture the standard output
        pythonProcess.stdout.on('data', (data) => {
            output += data.toString();
            // console.log(output)
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

//CHATTING
//CHATTING
//CHATTING
chats = "";

function AI(chat) {
    return new Promise((resolve, reject) => {
        const pythonProcess = spawn('python', ['python/ai.py', chat]);
        let output = '';

        // Capture the standard output
        pythonProcess.stdout.on('data', (data) => {
            output += data.toString();
            chats = output
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

//TIMETABLE PYTHON
//TIMETABLE PYTHON
//TIMETABLE PYTHON
slots = "";

function TimeTable(value) {
    return new Promise((resolve, reject) => {
        spawn('python', ['python/priority.py']);
        spawn('python', ['python/lpp.py']);
        spawn('python', ['python/specific.py']);
        const pythonProcess = spawn('python', ['python/timetable.py', value]);
        let output = '';

        // Capture the standard output
        pythonProcess.stdout.on('data', (data) => {
            output += data.toString();
            slots = output;
            console.log(slots);
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
})

router.get("/mcq/:topic", async(req, res, next) => {
    topic = req.params.topic;
    const tests = await test.findAll({
        where: { t: topic }
    });

    res.render('mcq', { title: 'mcq', tests, topic });
});



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

    await TestMCQ(req.body.t[0], marks.toString());


    marks = 0

    res.json({
        success: true,
        code: 200,
        result: result,
    });
})

//TIME CALCULATION
router.post("/time", async(req, res, next) => {
    console.log(req.body);

    const { topic, rating, time } = req.body;

    const statuses = await status.findOne({
        where: { id: 1 }
    })

    if (statuses) {
        const newTime = parseFloat(time) + parseFloat(statuses[`${topic}_time`]);

        await status.update({
            [`${topic}_time`]: newTime,
            [`${topic}_rating`]: rating
        }, { where: { id: 1 } });

        res.json({
            success: true,
            code: 200
        });
    } else {
        res.status(404).json({
            success: false,
            error: "Record not found",
            code: 404
        });
    }
})

router.get("/doc/:topic", async(req, res, next) => {
    const topic = req.params.topic;
    res.render('doc', { title: 'doc', topic })
})

router.get("/progress", async(req, res, next) => {
    const statuses = await status.findOne({
        where: { id: 1 }
    })
    res.render('progress', { title: 'progress', statuses })
})

router.post("/ai", async(req, res, next) => {
    await AI(req.body.message);
    console.log("---server---")
    console.log(chats)
    res.json({
        success: true,
        code: 200,
        result: chats
    });
})


router.post("/timetable", async(req, res, next) => {
    console.log(typeof(req.body.value))
    console.log(req.body.value)
    await TimeTable(req.body.value);
    res.json({
        success: true,
        code: 200,
        result: slots
    });
})

module.exports = router;