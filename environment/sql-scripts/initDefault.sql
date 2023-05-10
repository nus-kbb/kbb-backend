USE kbb_db;
INSERT INTO `project_table` (`id`, `project_name`, `status`, `content`, `created_on`) VALUES
(1,	'default',	'active',	'',	'2023-04-22 03:30:30') ON DUPLICATE KEY UPDATE `id` = 1;
INSERT INTO `user_table` (`id`, `user_email`, `project_id`, `user_password`, `role`, `created_on`) VALUES
(1,	'default@default.com',	1,	'default','admin', '2023-04-22 03:30:30') ON DUPLICATE KEY UPDATE `id` = 1;