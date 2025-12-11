-- SQL de ejemplo para crear las tablas principales (SQLite syntax simplificada)
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  is_admin BOOLEAN DEFAULT 0
);

CREATE TABLE books (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  isbn TEXT UNIQUE,
  total_copies INTEGER DEFAULT 1,
  available_copies INTEGER DEFAULT 1
);

CREATE TABLE loans (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  book_id INTEGER NOT NULL,
  loan_date TEXT,
  due_date TEXT,
  return_date TEXT,
  returned BOOLEAN DEFAULT 0
);

CREATE TABLE reservations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  book_id INTEGER NOT NULL,
  reserved_at TEXT,
  active BOOLEAN DEFAULT 1
);
