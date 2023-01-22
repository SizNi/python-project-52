INSERT INTO users_customuser (is_superuser, first_name, last_name, nickname, password, date_joined) VALUES ('False', 'first', 'last', 'nickasadsdolo', 'qwerty', 'today');
INSERT INTO users_customuser (is_superuser, email, first_name, last_name, nickname, password, date_joined) VALUES ('True', 'admin@mail.ru', 'admin', 'admin', 'admin', 'password', 'today');
superuser: administrator, password

INSERT INTO statuses_taskstatus (name, date_joined) VALUES ('test', 'today');
INSERT INTO tasks_task (name, description, created_date, creator_id, status_id, task_user_id) VALUES ('test', 'teeest', 'today', '2', '2', '2');
INSERT INTO tasks_task (name, description, created_date, creator_id, status_id, task_user_id) VALUES ('test_uest', 'teeest', 'today', '4', '2', '2');
INSERT INTO tasks_task (name, description, created_date, creator_id, status_id, task_user_id) VALUES ('test_3', 'teeest', 'today', '4', '5', '9');