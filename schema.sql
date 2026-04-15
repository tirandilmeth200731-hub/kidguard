DROP TABLE IF EXISTS child;
DROP TABLE IF EXISTS device;
DROP TABLE IF EXISTS activity;
DROP TABLE IF EXISTS blocked_site;

CREATE TABLE child (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    avatar TEXT
);

CREATE TABLE device (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    child_id INTEGER,
    name TEXT NOT NULL,
    type TEXT,
    screen_time_limit INTEGER, -- in minutes
    school_mode BOOLEAN DEFAULT 0,
    is_locked BOOLEAN DEFAULT 0,
    FOREIGN KEY(child_id) REFERENCES child(id)
);

CREATE TABLE activity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id INTEGER,
    app_name TEXT,
    duration INTEGER, -- in minutes
    date TEXT,
    FOREIGN KEY(device_id) REFERENCES device(id)
);

CREATE TABLE blocked_site (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL
);

-- Insert mock data
INSERT INTO child (name, age, avatar) VALUES ('Tommy', 9, '👦'), ('Emma', 13, '👧');
INSERT INTO device (child_id, name, type, screen_time_limit, school_mode, is_locked) VALUES 
(1, 'Tommy iPad', 'Tablet', 120, 1, 0),
(2, 'Emma iPhone', 'Phone', 180, 0, 0);

INSERT INTO activity (device_id, app_name, duration, date) VALUES 
(1, 'Minecraft', 45, date('now')),
(1, 'YouTube Kids', 30, date('now')),
(1, 'Roblox', 20, date('now')),
(2, 'TikTok', 90, date('now')),
(2, 'Instagram', 40, date('now')),
(2, 'Snapchat', 35, date('now'));

INSERT INTO blocked_site (url) VALUES 
('tiktok.com'),
('reddit.com'),
('discord.com');
