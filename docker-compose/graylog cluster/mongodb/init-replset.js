// This script executes the replicaset initialization until it succeeds

var rsConfig = {
  _id: "rs0",
  members: [
    { _id: 0, host: "10.32.134.76:27017" },
    { _id: 1, host: "10.32.133.198:27017" },
    { _id: 2, host: "10.32.138.166:27017" }
  ]
};

while (rs.initiate(rsConfig).ok === 0) {
  sleep(100);
}
