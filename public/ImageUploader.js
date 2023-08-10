const express = require("express");
const fileUpload = require("express-fileupload");
const sharp = require("sharp");
const path = require("path");
let app = express();
const port = 8080;

const https = require("https");
const fs = require("fs");

let key = fs.readFileSync("../config/tutorial.key", "utf-8");
let cert = fs.readFileSync("../config/tutorial.crt", "utf-8");

const parameters = {
  key: key,
  cert: cert,
};

// Add this line to serve our index.html page
app.use(express.static("public"));
app.use("/images", express.static(__dirname + "/images"));
app.get("/", function (req, res) {
  res.sendFile(path.join(__dirname, "./index.html"));
});

// default options
app.use(fileUpload());

app.post("/upload", function (req, res) {
  let red_side;
  let white_side;
  let orange_side;
  let yellow_side;
  let green_side;
  let blue_side;

  if (!req.files || Object.keys(req.files).length === 0) {
    return res.status(400).send("No files were uploaded.");
  }

  // The name of the input field (i.e. "red_side", "blue_side", ....) is used to retrieve the uploaded file
  red_side = {
    file: req.files.red_side,
    uploadPath: __dirname + "/cube_images/" + "red_side.jpg",
  };

  white_side = {
    file: req.files.white_side,
    uploadPath: __dirname + "/cube_images/" + "white_side.jpg",
  };

  orange_side = {
    file: req.files.orange_side,
    uploadPath: __dirname + "/cube_images/" + "orange_side.jpg",
  };

  yellow_side = {
    file: req.files.yellow_side,
    uploadPath: __dirname + "/cube_images/" + "yellow_side.jpg",
  };

  blue_side = {
    file: req.files.blue_side,
    uploadPath: __dirname + "/cube_images/" + "blue_side.jpg",
  };

  green_side = {
    file: req.files.green_side,
    uploadPath: __dirname + "/cube_images/" + "green_side.jpg",
  };

  fileArray = [
    red_side,
    yellow_side,
    blue_side,
    green_side,
    orange_side,
    white_side,
  ];
  totalSides = 0;
  // Use the mv() method to place the file somewhere on your server
  for (const fileObj of fileArray) {
    if (fileObj.file !== undefined) {
      totalSides += 1;
      console.log(fileObj.file.data);
      fileObj.file.data = sharp(fileObj.file.data).composite(
        [
          {input: __dirname + "/images/finalCubeMask2.png"}
        ]
      )
        .resize(200, 200)
        .toFile(fileObj.uploadPath, (err) => console.log(err));
        
      fileObj.file.mv(fileObj.uploadPath, function (err) {
        if (err) return res.status(500).send(err);
      });
    }
  }
  if (totalSides != 6) {
    return res.send(
      "sed life dude please upload something can't work with half assed cube"
    );
  }
  return res.send(
    "THANKS FOR UPLOADING FULL CUBE WAIT 200000000000 seconds to finish it."
  );
});

server = https.createServer(parameters, app);
server.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
