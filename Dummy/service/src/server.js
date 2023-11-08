const express = require("express");
const bodyParser = require("body-parser");
const flagService = require("./flag");
const app = express();

app.use(
  bodyParser.urlencoded({
    extended: true,
  })
);
app.use(express.json());

PORT = 5001;

const log = (msg) => {
  const currentDate = new Date().toUTCString();
  console.log(`[${currentDate}] ${msg}`);
};

app.get("/", (_req, res) => {
  log("GET on /");
  res.send("I am just a dummy Vulnbox");
});

app.get("/ping", (_req, res) => {
  log("GET on /ping");
  res.send("I am just a dummy Vulnbox");
});

app.get("/get", (req, res) => {
  log("GET on /get");

  const expectedAuth = `Bearer ${process.env.FLAG_MANAGER_SECRET}`;
  if (
    !req.headers ||
    !req.headers.authorization ||
    req.headers.authorization !== expectedAuth
  ) {
    res.send("Unauthorized");
  }

  if (req.query && req.query.id && req.query.vuln) {
    log(`Received id: ${req.query.id} - vuln: ${req.query.vuln}`);
    const id = req.query.id;
    const vuln = req.query.vuln;
    res.json({ flag: flagService.getFlag(id, vuln) });
  } else {
    res.send("ERROR: unable to get flag");
  }
});

app.post("/put", (req, res) => {
  log("POST on /put");

  const expectedAuth = `Bearer ${process.env.FLAG_MANAGER_SECRET}`;
  if (
    !req.headers ||
    !req.headers.authorization ||
    req.headers.authorization !== expectedAuth
  ) {
    res.send("Unauthorized");
  }

  if (req.body && req.body.id && req.body.vuln && req.body.flag) {
    log(
      `Received body with id: ${req.body.id} - vuln: ${req.body.vuln} - flag: ${req.body.flag}`
    );
    const id = req.body.id;
    const vuln = req.body.vuln;
    const flag = req.body.flag;

    flagService.setFlag(id, vuln, flag);
    res.send("Flag correctly set");
  } else {
    res.send("ERROR: flag not set");
  }
});

app.get("/hackme", (_req, res) => {
  log("GET on /hackme");
  res.json({ flag: flagService.getLastFlag() });
});

log(`Starting Dummy ForcAD Vulnbox on port ${PORT}`);
app.listen(PORT);
