const express = require("express");
const fileUpload = require("express-fileupload");
const path = require("path");
const app = express();
const port = 3000;

// Add this line to serve our index.html page
app.use(express.static("public"));
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
  let uploadPath;

  if (!req.files || Object.keys(req.files).length === 0) {
    return res.status(400).send("No files were uploaded.");
  }

  // The name of the input field (i.e. "red_side", "blue_side", ....) is used to retrieve the uploaded file
  red_side = {
    file: req.files.red_side,
    uploadPath: __dirname + "/images/" + "red_side.jpg",
  };
  console.log(red_side);

  white_side = {
    file: req.files.white_side,
    uploadPath: __dirname + "/images/" + "white_side.jpg",
  };
  console.log(white_side);

  orange_side = {
    file: req.files.orange_side,
    uploadPath: __dirname + "/images/" + "orange_side.jpg",
  };
  console.log(orange_side);

  yellow_side = {
    file: req.files.yellow_side,
    uploadPath: __dirname + "/images/" + "yellow_side.jpg",
  };
  console.log(yellow_side);

  blue_side = {
    file: req.files.blue_side,
    uploadPath: __dirname + "/images/" + "blue_side.jpg",
  };
  console.log(blue_side);

  green_side = {
    file: req.files.green_side,
    uploadPath: __dirname + "/images/" + "green_side.jpg",
  };
  console.log(green_side);

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

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});