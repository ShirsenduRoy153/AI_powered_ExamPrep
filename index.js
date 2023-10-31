const express = require("express")
const app = express()
const path = require("path")
const hbs = require("hbs")


const tempelatePath = path.join(__dirname, "templates")

app.use(express.json())
app.set("view engine", "hbs")
app.set("views", tempelatePath)
app.use(express.urlencoded({ extended: false }))



//------------------------------MAIN.js--------------------------//
const { spawn } = require('child_process');
const { timeStamp } = require('console');

function runPythonFunction() {
    const pythonProcess = spawn('python', ['final.py']);

    // Listen for the standard output of the Python script
    pythonProcess.stdout.on('data', (data) => {
        const result = data.toString().trim();
        console.log('Result:', result);
        //hi(result);
    });

    // Listen for errors, if any
    pythonProcess.stderr.on('data', (data) => {
        console.error('Error:', data.toString());
    });

    // Handle process exit
    pythonProcess.on('close', (code) => {
        console.log(`Python script exited with code ${code}`);
    });
    console.log("listening . . .")
}
// Call the Python function
//runPythonFunction();

//----------------------------------------------//this part is for DATABASE calling




/*function hi(result) {
    rs = "helllllll" + result
    console.log("--extra added------",
        rs)
}*/
//-----------------------------------------------------//

//-------------------GET-------------------//

app.get('/', (req, res) => {
    res.render('voice')
})

app.get('/voice', (req, res) => {
    res.render('voice')
})

//-------------------POST-----------------//

app.post('/voice', async(req, res) => {

    console.log("hello")
    await runPythonFunction();
    res.render("voice")
})

app.listen(3000, () => {
    console.log("Port Connected...")
})