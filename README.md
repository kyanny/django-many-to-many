```
❯ sqlite3 db.sqlite3
SQLite version 3.28.0 2019-04-15 14:49:49
Enter ".help" for usage hints.
sqlite> .table
auth_group                  bookmark_tags
auth_group_permissions      django_admin_log
auth_permission             django_content_type
auth_user                   django_migrations
auth_user_groups            django_session
auth_user_user_permissions  tag
bookmark
sqlite> .schema bookmark
CREATE TABLE IF NOT EXISTS "bookmark" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "url" text NOT NULL);
sqlite> .schema tag
CREATE TABLE IF NOT EXISTS "tag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" text NOT NULL);
sqlite> .schema bookmark_tags
CREATE TABLE IF NOT EXISTS "bookmark_tags" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "bookmark_id" integer NOT NULL REFERENCES "bookmark" ("id") DEFERRABLE INITIALLY DEFERRED, "tag_id" integer NOT NULL REFERENCES "tag" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "bookmark_tags_bookmark_id_tag_id_6d770b6c_uniq" ON "bookmark_tags" ("bookmark_id", "tag_id");
CREATE INDEX "bookmark_tags_bookmark_id_89db5e43" ON "bookmark_tags" ("bookmark_id");
CREATE INDEX "bookmark_tags_tag_id_d6e5d3c3" ON "bookmark_tags" ("tag_id");
```
