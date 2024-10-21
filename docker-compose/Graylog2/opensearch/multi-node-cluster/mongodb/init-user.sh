#!/bin/bash

mongo <<EOF

   use admin;
   
   admin = db.getSiblingDB("admin");

   admin.createUser(
      {
         user: "admin",
         pwd: "xFusion@12#$",
         roles: [
            {role: "root", db: "admin"}
         ]
      }
   );

   sleep 2

   db.auth("admin", "xFusion@12#$");

   use graylog;
   
   db.createUser(
      {
         user: "graylog",
         pwd: "Graylog@12#$",
         roles: [
            {"role":"readWrite","db":"graylog"},
            {"role":"dbAdmin","db":"graylog"}	
         ]
      }
   );
   
   sleep 2

   db.auth("graylog", "Graylog@12#$");
   
   rs.status();

EOF
