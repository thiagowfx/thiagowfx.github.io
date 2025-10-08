---
title: "MongoDB: find idle connections"
date: 2024-05-07T14:45:00+02:00
tags:
  - dev
---

**Problem statement**: Find idle connections on Atlas MongoDB.

We'll use NodeJS (`node`, `npm`) to do so.

`package.json`:

```json
{
  "devDependencies": {
    "mongodb": "^6.6.1",
    "nodemon": "^3.1.0"
  },
  "scripts": {
    "start:dev": "nodemon main.js"
  }
}
```

Install dependencies via `npm ci` (or simply `npm install`).

Use `nodemon` to automatically restart the node process upon script changes – it
is a file watcher daemon. Great when developing and iterating locally, for
incremental changes.

`main.js`:

```js
#!/usr/bin/env node

const {MongoClient, ServerApiVersion} = require("mongodb");

// REPL: `mongosh <uri>`
const uri = "mongodb+srv://{user}:{password}@{host}.mongodb.net/?retryWrites=true&w=majority&appName={redacted}";

const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    deprecationErrors: true,
  },
});

async function run() {
  try {
    await client.db("test").command({
      ping: 1
    });
    console.log("Successfully connected to MongoDB!");

    const serverStatus = await client.db("test").command({
      serverStatus: 1
    });

    console.log(`Active connections: ${serverStatus.connections.active}`);
    console.log(
      `Idle connections: ${serverStatus.connections.current - serverStatus.connections.active}`,
    );

    const currentOp = await client
      .db("admin")
      .aggregate([
        {
          $currentOp: {
            allUsers: true,
            idleSessions: true,
          },
        },
        {
          $match: {
            type: "idleSession",
          },
        },
      ]);
    console.log(currentOp);
  } finally {
    await client.close();
  }
}
run().catch(console.dir);
```
