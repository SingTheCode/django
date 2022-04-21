SELECT COUNT(*) FROM users_user;

SELECT * FROM users_user;

SELECT "users_user"."id",
       "users_user"."first_name",
       "users_user"."last_name",
       "users_user"."age",
       "users_user"."country",
       "users_user"."phone",
       "users_user"."balance"
  FROM "users_user";

  INSERT INTO "users_user" ("first_name", "last_name", "age", "country", "phone", "balance") SELECT '길동',
       '홍',
       100,
       '제주도',
       '010-1234-1234',
       10000 RETURNING "users_user"."id";
       
  INSERT INTO "users_user" VALUES
  (102, '길동', '김', 100, '경상북도', '010-1234-1234', 100);

  SELECT * FROM users_user WHERE id=101;

  UPDATE users_user
  SET first_name='철수'
  WHERE id=101;

  DELETE
    FROM "users_user"
   WHERE "users_user" ."id" IN(102)

  SELECT COUNT(*) FROM users_user;

  SELECT "users_user"."id",
        "users_user"."first_name",
        "users_user"."last_name",
        "users_user"."age",
        "users_user"."country",
        "users_user"."phone",
        "users_user"."balance"
    FROM "users_user"
  WHERE "users_user"."age" = 30

  SELECT COUNT(*) AS "__count"
    FROM "users_user"
  WHERE "users_user"."age" <= 30

  SELECT COUNT(*) AS "__count"
    FROM "users_user"
  WHERE "users_user"."age" < 30

  SELECT COUNT(*) AS "__count"
    FROM "users_user"
  WHERE "users_user"."age" > 30

  SELECT COUNT(*) AS "__count"
  FROM "users_user"
 WHERE ("users_user"."age" = 30 AND "users_user"."last_name" = '김')

  SELECT "users_user"."id",
        "users_user"."first_name",
        "users_user"."last_name",
        "users_user"."age",
        "users_user"."country",
        "users_user"."phone",
        "users_user"."balance"
    FROM "users_user"
  WHERE ("users_user"."age" = 30 OR "users_user"."last_name" = '김')