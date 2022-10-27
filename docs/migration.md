# Initial data migration

1. Create .env file and define the following
  - DB_HOST
  - DB_PORT
  - DB_NAME
  - DB_USER
  - DB_PASS
  - DB_ROOT_PASS

2. Alter the SQL dump: change the sql so that only one database is created and that the database name matches `DB_NAME`. Originally the `log` table is in a different database.

3. Change `entrypoint.sh` so `migrate` is run with `--fake-initial` option.

4. Run `docker-compose up --build --no-start`, then start only the database container. Use a mysql client to run the sql commands to recreate the database (e.g. running locally `mysql -u {DB_USER} -p{DB_PASS} -h 0.0.0.0 -P {PORT} < sql_file.sql`, check `docker ps` for the db port mapping)

5. Start the other containers and export the data if necessary.
