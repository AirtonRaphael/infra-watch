CREATE TABLE PermissionType (
    permission_id INTEGER PRIMARY KEY,
    permission_type TEXT NOT NULL UNIQUE
);


CREATE TABLE User (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    hash_password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    permission_id INTEGER,
    FOREIGN KEY (permission_id) REFERENCES PermissionType(permission_id)
);


INSERT INTO PermissionType (permission_type)
VALUES ('User'), ('Admin');


INSERT INTO User (username, hash_password, email, permission_id)
VALUES (
    'admin',
    '$2b$12$nfdNjajPaqAZ83fqn3UsHe/7.aPy/6XG8H0v2J6un4H0iEZNRrECa',
    'admin@admin.com',
    (SELECT permission_id FROM PermissionType WHERE permission_type = 'Admin')
);

-- hosts
CREATE TABLE Hosts (
    host_id INTEGER PRIMARY KEY,
    label VARCHAR(255) UNIQUE NOT NULL,
    endpoint NVARCHAR(255) NOT NULL
);


-- Logs
