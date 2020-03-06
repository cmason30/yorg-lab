CREATE TABLE "mouses" (
  "mouse_id" SERIAL PRIMARY KEY,
  "category" text,
  "filename" text
);

CREATE TABLE "experiments" (
  "exp_id" SERIAL PRIMARY KEY,
  "original_file" text,
  "experiment_file_name" text,
  "r2" float,
  "k_vals" float,
  "tau_vals" float,
  "Half_Life" float,
  "selected_area" float,
  "t20" float,
  "t80" float,
  "half_width" float,
  "peak_height" float,
  "DAc" float,
  "rise_time" float,
  "rising_slope" float,
  "mouse_id" int
);

CREATE TABLE "intervals" (
  "int_id" SERIAL PRIMARY KEY,
  "time" float,
  "current_nA" float,
  "exp_id" int
);

ALTER TABLE "experiments" ADD FOREIGN KEY ("mouse_id") REFERENCES "mouses" ("mouse_id");

ALTER TABLE "intervals" ADD FOREIGN KEY ("exp_id") REFERENCES "experiments" ("exp_id");
